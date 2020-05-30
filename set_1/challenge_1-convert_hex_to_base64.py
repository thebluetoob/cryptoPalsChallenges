#!/usr/bin/env python3

# https://cryptopals.com/sets/1/challenges/1

# The string:
# 49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
# 
# Should produce:
# SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t
#
# Cryptopals Rule:
# Always operate on raw bytes, never on encoded strings. Only use hex and base64 for pretty-printing.

import base64

original_hex = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'

raw_bytes = bytes.fromhex(original_hex)

encoded_bytes = base64.b64encode(raw_bytes)

print('Input: ' + original_hex)
print('Decoded message (from hex): ' + raw_bytes.decode())
print('Encoded message (to base64): ' + encoded_bytes.decode())

# Output:
# Input: 49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
# Decoded message (from hex): I'm killing your brain like a poisonous mushroom
# Encoded message (to base64): SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t