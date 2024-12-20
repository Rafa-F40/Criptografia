import json
import base64
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

#Cifrado
textoPlano_bytes = bytes('He descubierto el error y no volveré a hacerlo mal', 'UTF-8')
clave = bytes.fromhex('E2CFF885901B3449E9C448BA5B948A8C4EE322152B3F1ACFA0148FB3A426DB74')
nonce = base64.b64decode("9Yccn/f5nJJhAt2S")
datos_asociados_bytes = bytes("", "UTF-8")

cipher = AES.new(clave, AES.MODE_GCM,nonce=nonce)
cipher.update(datos_asociados_bytes)
texto_cifrado_bytes, tag = cipher.encrypt_and_digest(textoPlano_bytes)

hexa = texto_cifrado_bytes.hex()
base = b64encode(texto_cifrado_bytes).decode('UTF-8')
tag_pr = tag.hex()
tag_pr_b64 = b64encode(tag).decode('UTF-8')

print("El texto en hexadecimal es:", hexa)
print("El texto en Base64 es:", base)
print("El tag en hexadecimal es:", tag_pr)
print("El tag en Base64 es:", tag_pr_b64)



