# Typosquatted Domain Name Searcher
Search for unregistered typosquatted domain names using homoglyphs and then filter based on the similarity with the original domain name using computer vision.

<p align="center">
<img src="https://github.com/tur11ng/typosquatted-domain-name-searcher/assets/61602820/5022c404-b387-4ff1-9fd5-d3a25221ee5a" width="700" />
</p>

### Requirements
    Python 3.10+
    Nmap   7.94+ (other versions will probably work too.)

### Installation
```
git clone https://github.com/tur11ng/typosquatted-domain-name-searcher
cd typosquatted-domain-name-searcher
virtualenv ./venv
chmod u+x ./venv/bin/activate
source ./venv/bin/activate
pip install -r requirements.txt
```

### Execution
```
python3 main.py example.com Android
python3 main.py -h
```

### Functionality

Checking if a domain name is registered or not isn't straight forward due to privacy laws restrictions which forbid TLDs from
having WHOIS servers. This problem is pretty common in EU. 

We apply some heuristics to check if a domain is registered using the following steps, if any of them succeeds we assume that it is registered.

1. Check if it responds to DNS lookups.
2. Check if a WHOIS lookup succeeds.
3. Check if the top 10 common ports are open.
4. Check if it responds to HTTP/HTTPS requests. (This is redundant and will be removed.)

If a domain name is found unregistered, we then evaluate it's visual similarity with the original one using the SSIM index. 
