import requests

def fetch(url):
    r = requests.get(url, timeout=15)
    r.raise_for_status()
    return r.text
