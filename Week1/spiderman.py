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
        print("Test","https://spiderman.quoccacorp.com/" + url)
        
        r = requests.get("https://spiderman.quoccacorp.com/" + url, proxies=proxies, verify=False)
        flag = re.search("COMP6443",r.text)
        if flag:
          return flag.group(0)
        results = re.findall("href=\"[^\"]*\"", r.text)
        print(results)
        queue.extend(results)



print(spiderman())