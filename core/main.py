__author__ = 'la0rg'

import requests

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36'}
post_data = {
    'ajxrequest': '0',
    'pollid': '27',
    'idf': 'easypoll',
    'poll_choice': '511',
    'submit': 'Голосовать'
}

proxies = []

proxies_file = open('proxies.txt', 'r')

for line in proxies_file:
    #proxies.append({"http": "http://" + line.strip("\t\n")})
    proxies.append({"http": "http://" + line.replace('\t', ':').strip("\t\n")})
    #proxies.append({"https": "https://" + line.strip("\t\n")})

print(proxies)

errors = 0
for proxy in proxies:
    try:
        print(requests.post("http://ap.tomsk.ru/contest/227-14.html?showresults=1", headers=headers, data=post_data, proxies=proxy, timeout=10))
    except:
        errors += 1
        print("timeout")
print("Errors:{0}/{1}, Responded: {2}".format(errors, len(proxies), len(proxies) - errors))
