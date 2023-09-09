# Homoglyph Domain Searcher
Search for domain name lookalikes using homoglyphs.

### Requirements
    Python 3.10+
    Nmap   7.94+ (other versions will probably work too.)

### Installation
```
git clone https://github.com/tur11ng/homoglyph-domain-searcher
cd homoglyph-domain-searcher
virtualenv ./venv
chmod u+x ./venv/bin/activate
source ./venv/bin/activate
pip install -r requirements.txt
python3 main.py example.com
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
