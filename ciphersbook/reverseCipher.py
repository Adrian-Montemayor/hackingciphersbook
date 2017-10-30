# Reverse Cipher

message = input("What's your message?\n ")
translated = '' 

i = len(message) - 1
while i >= 0:
	translated = translated + message[i]
	print(i, message[i], translated)
	i -= 1

print(translated)
