import simplecrypt

with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()

with open("passwords.txt", "r") as pw:
    passes = pw.readlines()



for password in passes:

    try:
        s = simplecrypt.decrypt(password.strip(), encrypted)

    except simplecrypt.DecryptionException:
            pass
    else:
        print(s.decode('UTF-8'))

