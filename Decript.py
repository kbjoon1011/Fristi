import base64, codecs

def DecryptPass(str):
    str = codecs.decode(str, 'rot13')
    str = base64.b64decode(str[::-1])
    return str


decryptedpass = DecryptPass("mVGZ3O3omkJLmy2pcuTq")
whoisgod = DecryptPass("=RFn0AKnlMHMPIzpyuTI0ITG")

print(decryptedpass)
print("=" *20)

print(whoisgod)