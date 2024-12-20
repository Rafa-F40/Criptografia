from Crypto.Cipher import ChaCha20_Poly1305
import base64
from base64 import b64encode, b64decode
from Crypto.Cipher import ChaCha20
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import jks
import os

path = os.path.dirname(__file__)

keystore = path + "/KeyStorePracticas"


ks = jks.KeyStore.load(keystore, "123456")

for alias, sk in ks.secret_keys.items():
    if sk.alias == "cifrado-sim-chacha20-256":
        key = sk.key


try:

    textoPlano = bytes('KeepCoding te enseña a codificar y a cifrar', 'UTF-8')
    clave = key
    #Como mejora usamos un nonce aleatorio
    nonce_mensaje = get_random_bytes(12)
    #Para añadir aun mas seguridad añadimos datos asociados y garantizamos la integridad del mensaje
    datos_asociados = bytes('Prueba educativa no usar en la vida real', 'utf-8')
    cipher = ChaCha20_Poly1305.new(key=clave, nonce=nonce_mensaje)
    cipher.update(datos_asociados)
    texto_cifrado, tag = cipher.encrypt_and_digest(textoPlano)
    print('Mensaje cifrado en HEX = ', texto_cifrado.hex())
    print('Mensaje cifrado en B64 = ', base64.b64encode(texto_cifrado).decode())

    
    #Descifrado para comprobar el aumento de seguridad con los datos asociados

    decipher = ChaCha20_Poly1305.new(key=clave, nonce=nonce_mensaje)
    datos_asociados_fake = bytes("No tengo ni idea, Hulio...","utf-8")
    decipher.update(datos_asociados_fake)
    #decipher.update(datos_asociados_fake)
    plaintext = decipher.decrypt_and_verify(texto_cifrado,tag)
    #plaintext = decipher.decrypt_and_verify(texto_cifrado_fake,tag)
    print('Datos cifrados en claro = ',plaintext.decode('utf-8'))
except (ValueError, KeyError) as error: 
     print("Problemas al descifrar....")
     print("El motivo del error es: ", error)