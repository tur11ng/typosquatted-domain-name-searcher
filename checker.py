import socket

import requests
import whois
import nmap


class Checker:
    @staticmethod
    def is_domain_name_registered(domain_name: str) -> bool:
        try:
            if socket.gethostbyname(domain_name):
                return True
        except socket.gaierror:
            pass

        try:
            if domain_name.split(".")[-1:] in whois.validTlds():
                if whois.query(domain_name):
                    return True
        except Exception:
            pass

        top_ports = '21,22,23,25,53,80,110,135,139,443'
        nm = nmap.PortScanner()
        nm.scan(domain_name, top_ports)

        if domain_name in nm.all_hosts():
            for proto in nm[domain_name].all_protocols():
                for port in nm[domain_name][proto].keys():
                    if (nm[domain_name][proto][port]["state"] == "open"
                            or nm[domain_name][proto][port]["state"] == "filtered"):
                        return True

        try:
            if requests.get(f"http://{domain_name}"):
                return True
            if requests.get(f"https://{domain_name}"):
                return True
        except requests.exceptions.RequestException:
            pass

        return False
