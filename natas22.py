import requests
address = "http://natas22:chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ@natas22.natas.labs.overthewire.org/"

r = requests.get(address+'?revelio', allow_redirects = False)
print(r.status_code)
if r.status_code == 302:
	print(r.text)
