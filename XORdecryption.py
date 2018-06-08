from __future__ import print_function, unicode_literals
from os import urandom

decrypted = xor_strings(cipherText, key).decode('utf8')