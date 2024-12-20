from Crypto.Protocol.KDF import HKDF
from Crypto.Hash import SHA512
import secrets
import jks
import os


path = os.path.dirname(__file__)

keystore = path + "/KeyStorePracticas"


ks = jks.KeyStore.load(keystore, "123456")

for alias, sk in ks.secret_keys.items():
    if sk.alias == "cifrado-sim-aes-256":
        key = sk.key

print("La clave es maestra es:", key.hex())


salt = bytes.fromhex("e43bb4067cbcfab3bec54437b84bef4623e345682d89de9948fbb0afedc461a3")
master_secret = key
key1 = HKDF(master_secret, 32, salt, SHA512, 1)

print("Clave Diversificada: ", key1.hex())
