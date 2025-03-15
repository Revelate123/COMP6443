import requests

proxies = {
  'https': 'http://127.0.0.1:8080',
}
requests.packages.urllib3.disable_warnings() 

with open("Week3/Signin/directory-list-2.3-small.txt") as f:
    for line in f:
        data = line.strip('\n')
        print()
        r = requests.get("https://signin.quoccacorp.com/v3"+data,proxies=proxies, verify=False)
        if r.status_code == 200:
            print(data)
        
