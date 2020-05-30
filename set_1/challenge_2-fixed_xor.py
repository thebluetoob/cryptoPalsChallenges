#!/usr/bin/env python3

# https://cryptopals.com/sets/1/challenges/2

# Write a function that takes two equal-length buffers and produces their XOR combination.
# 
# If your function works properly, then when you feed it the string:
# 
# 1c0111001f010100061a024b53535009181c
# ... after hex decoding, and when XOR'd against:
# 
# 686974207468652062756c6c277320657965
# ... should produce:
# 
# 746865206b696420646f6e277420706c6179

import binascii

def byte_xor(ba1, ba2):
    return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])

ciphertext_hex = '1c0111001f010100061a024b53535009181c'

xor_key_hex = '686974207468652062756c6c277320657965'

ciphertext_bytes = bytes.fromhex(ciphertext_hex)

xor_key_bytes = bytes.fromhex(xor_key_hex)

plaintext = byte_xor(ciphertext_bytes, xor_key_bytes).decode()

plaintext_hex = binascii.hexlify(plaintext.encode('utf8'))

print('Original ciphertext: ' + ciphertext_hex)
print('Provided XOR key: ' + xor_key_hex)
print('Plaintext: ' + plaintext)
print('Encoded plaintext: ' + plaintext_hex.decode())
