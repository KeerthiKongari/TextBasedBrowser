import sys, os
import requests
 
# write your code here
def check_url(site):
    url = site if site.startswith("https://") else "https://" + site
    return url
 
def get_data_by_url(url):
    url = check_url(url)
    req = requests.get(url)
    return req.text
 
if len(sys.argv) == 2:
    directory_name = sys.argv[1]
 
    path = ".\\" + directory_name
 
    if not os.path.isdir(path):
        os.mkdir(path)
 
# record of browser history
history = []
 
choice = -1
while choice != 0:
 
    url = input()
    content = None
 
    if url == "exit":
        choice = 0
 
    elif url == "back":
        history.pop()
        if history:
            
            if history[-1] == "bloomberg":
                content = bloomberg_com
 
            elif history[-1] == "nytimes":
                content = nytimes_com
 
            print(content)
 
    elif url.count('.') != 0:
 
        tokens = url.split('.')
        content = get_data_by_url(url)
 
        print(content)
 
        # add current website into browser history
        web_name = tokens[0]
        history.append( web_name )
 
 
        with open(path + "/" + web_name, 'w') as f:
            f.write(content)
 
    elif url in history:
 
        web_name = url
        with open(path + "/" + web_name, 'r') as f:
            content = f.read()
            print(content)
 
    else:
        print('Error: Incorrect URL')