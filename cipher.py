import random

def generate_key():
	key = [c for c in "abcdefghijklmnopqrstuvwxyz"]
	random.shuffle(key)
	return  "".join(key)

def encrypt(plaintext, key):
	ciphertext = ""
	for c in plaintext.lower():
		if c.isalpha():
			ciphertext += key[ord(c) - ord('a')]
		else:
			ciphertext += c
	return ciphertext

def decrypt(ciphertext, key):
	plaintext = ""
	for c in ciphertext:
		if c.isalpha():
			plaintext += chr(key.index(c) + ord('a'))
		else:
			plaintext += c
	return plaintext
