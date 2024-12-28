import random
import string

chars = " "+ string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

#Encryption
plain_text = input("Enter a message: ")
cypher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cypher_text = key[index] + cypher_text

print(f"Original Message: {plain_text}")
print(f"Encrypted Message: {cypher_text}")

#Decryption
cypher_text = input("Enter a message: ")
plain_text = ""

for letter in cypher_text:
    index = key.index(letter)
    plain_text = chars[index] + plain_text

print(f"Encrypted Message: {cypher_text}")
print(f"Original Message: {plain_text}")