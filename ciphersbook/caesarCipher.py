import pyperclip

#The string to be encrypted/decrypted
message = input("What's your secret message?: ")

#The encryption/decription key
key = 13

#Tells te program to encrypt or decrypt
mode = input('Select a mode encrypt/decrypt: ')

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# stores the encrypted/decrypted from of the message

translated = ''

# capitalize the string in message

message = message.upper()

for symbol in message:
	if symbol in LETTERS:
		num = LETTERS.find(symbol)
		if mode == 'encrypt':
			num = num + key
		elif mode == 'decrypt':
			num = num - key
		if num >= len(LETTERS):
			num = num - len(LETTERS)
		elif num < 0:
			num = num + len(LETTERS)
		translated = translated  + LETTERS[num]
	else: 
		translated = translated + symbol
print('Key #%s: %s' % (key, translated))
#pyperclip.copy(translated)

