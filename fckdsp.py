import sys
from binascii import a2b_base64

from Cryptodome.Cipher import AES

# args: key vi file_path
if len(sys.argv) < 4:
    print("4 argv needed: key vi file_path")
    exit()

key, iv, file_path = sys.argv[1].encode(), sys.argv[2].encode(), sys.argv[3]
print(key, iv, file_path)

with open(file_path, 'r') as f:
    code_base64 = f.read()

aes = AES.new(key, AES.MODE_CBC, iv)
decrypt_aes = AES.new(key, AES.MODE_CBC, iv)
text = bytes.decode(decrypt_aes.decrypt(a2b_base64(code_base64)))
print(text)

with open(file_path.replace('.dsp', '') + '.xml', 'w') as f:
    f.write(text)
