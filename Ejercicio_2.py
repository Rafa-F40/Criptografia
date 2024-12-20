from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import jks
import os

path = os.path.dirname(__file__)

keystore = path + "/KeyStorePracticas"


ks = jks.KeyStore.load(keystore, "123456")

for alias, sk in ks.secret_keys.items():
    if sk.alias == "cifrado-sim-aes-256":
        key = sk.key


texto_cifrado_bytes=b64decode('TQ9SOMKc6aFS9SlxhfK9wT18UXpPCd505Xf5J/5nLI7Of/o0QKIWXg3nu1RRz4QWElezdrLAD5LO4USt3aB/i50nvvJbBiG+le1ZhpR84oI=')
clave_d = key
iv_d=bytes.fromhex('00000000000000000000000000000000')
cipher_d=AES.new(clave_d,AES.MODE_CBC,iv_d)
mensaje_claro_padding=cipher_d.decrypt(texto_cifrado_bytes)

print(mensaje_claro_padding.hex())

mensaje_claro=unpad(mensaje_claro_padding,AES.block_size,style="pkcs7")
print(mensaje_claro.decode("UTF-8"))

mensaje_claro2=unpad(mensaje_claro_padding,AES.block_size,style="x923")
print("En este caso se pueden usar los 2 padding:", mensaje_claro2.decode("UTF-8"))
