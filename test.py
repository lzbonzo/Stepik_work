

from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

key = b'abcdefgh'
def pad(text):
    while len(text) % 8 != 0:
        text += b' '
    return text

des = DES.new(key, DES.MODE_ECB)
text = b'Python Rocks!'
paddet_text = pad(text)

encrypted_text = des.encrypt(paddet_text)
print(encrypted_text)