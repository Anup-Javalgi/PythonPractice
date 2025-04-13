# Encryption program in Python

import random
import string

chars = " " + string.whitespace + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()
random.shuffle(key)

print(f"key : {key}")
print(f"chars : {chars}")

# Encrypt
plain_text  = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    indexs = chars.index(letter)
    cipher_text+=key[indexs]

print(f"Plain text : {plain_text}")
print(f"Cipher text : {cipher_text}")

# Decrypt
decrypt_text = ""
for cipher in cipher_text:
    indexs = key.index(cipher)
    decrypt_text+=chars[indexs]

print(f"Decrypted text : {decrypt_text}")