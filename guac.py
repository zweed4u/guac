#!/usr/bin/env python2.7
import json,requests
url='https://api-proxy.chipotle.com/guacsmash/reg'
first=raw_input('First name: ')
last=raw_input('Last name: ')
cell=raw_input('Cell Phone: (eg. 5858675309) ')
zipcode=raw_input('Zip code: ')
headers={
	'Accept':'application/json',
	'Accept-Encoding':'gzip, deflate, br',
	'Accept-Language':'en-US,en;q=0.8',
	'Connection':'keep-alive',
	'Content-Type':'application/json',
	'Host':'api-proxy.chipotle.com',
	'Origin':'https://cado-crusher.chipotle.com',
	'Referer':'https://cado-crusher.chipotle.com/',
	'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/55.0.2883.87 Chrome/55.0.2883.87 Safari/537.36'
}
session=requests.session()
data={
	'f':first,
	'l':last,
	'm':cell,
	's':'false',
	'z':zipcode,
}
r=session.post(url,json=data,headers=headers)
print r.json()