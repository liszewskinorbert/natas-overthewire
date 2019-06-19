#!/usr/bin/env python

import requests
import re
import urllib
import base64

username = 'natas11'
password = 'U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK'


url = 'http://%s.natas.labs.overthewire.org' % username

session = requests.Session()
#response = session.get(url, auth = (username, password))
#cookie = session.cookies['data']
#cookieurl = (urllib.unquote(cookie))

#print(base64.b64decode(cookieurl).encode('hex'))

#print(re.findall('/etc/natas_webpass/natas11:(.*)', content)[0])

cookies = {"data" : "ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK" }
response = session.get(url, auth = (username, password), cookies = cookies)
content=response.text

print(content)
