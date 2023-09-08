import socket

import homoglyphs as hg

import argparse
import sys
import itertools

import requests
import validators
import whois
import nmap


def typosquatted_domain_name_generator(domain_name: str):
    tld = domain_name[domain_name.rfind('.'):]
    domain_name = domain_name[:domain_name.rfind('.')]

    letters_homoglyphs = []

    for letter in domain_name:
        if letter == '.':
            letters_homoglyphs += '.'
            continue
        letters_homoglyphs += [hg.Homoglyphs().get_combinations(letter)]

    for typosquatted_domain_name in itertools.product(*letters_homoglyphs):
        typosquatted_domain_name_str = ''.join(typosquatted_domain_name) + tld
        if validators.domain(typosquatted_domain_name_str):
            yield typosquatted_domain_name_str


def is_registered(domain_name: str) -> bool:
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
                if nm[domain_name][proto][port]["state"] == "open":
                    return True

    try:
        if requests.get(f"http://{domain_name}"):
            return True
        if requests.get(f"https://{domain_name}"):
            return True
    except requests.exceptions.RequestException:
        pass

    return False


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('domain_name', type=str, help='The \
                        domain name to search for typosquatting alternatives.')
    args = parser.parse_args(sys.argv[1:])

    domain_name = args.domain_name
    if not validators.domain(domain_name):
        raise Exception(
            'Invalid domain name. Check that the domain name you provided complies with RFCs 1034, 1035, 2181'
        )

    for typosquatted_domain_name in typosquatted_domain_name_generator(domain_name):
        if not is_registered(typosquatted_domain_name):
            print(typosquatted_domain_name)


if __name__ == '__main__':
    main()
