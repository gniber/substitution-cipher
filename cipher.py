import random

def generate_key():
	key = [c for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
	random.shuffle(key)
	return  "".join(key)

def encrypt(plaintext, key):
	ciphertext = ""
	key = key.upper()
	for c in plaintext.upper():
		if c.isalpha():
			ciphertext += key[ord(c) - ord('A')]
		else:
			ciphertext += c
	return ciphertext

def decrypt(ciphertext, key):
	plaintext = ""
	key = key.upper()
	for c in ciphertext.upper():
		if c.isalpha():
			plaintext += chr(key.index(c) + ord('A'))
		else:
			plaintext += c
	return plaintext
