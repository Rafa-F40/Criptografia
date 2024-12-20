from ssl import VerifyFlags
import jwt
import base64 
from base64 import b64encode, b64decode


Head_comun=base64.b64decode("eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9").decode("UTF-8")
print("El Head común es", Head_comun)

#Este paso da error por lo que comentamos del Base64url
#Bytes_legitimos = base64.b64decode("eyJ1c3VhcmlvIjoiRG9uIFBlcGl0byBkZSBsb3MgcGFsb3RlcyIsInJvbCI6ImlzTm9ybWFsIiwiaWF0IjoxNjY3OTMzNTMzfQ")
#Body_legitimo = Bytes_legitimos.decode("utf-8")
#print("El Body legítimo es:", Body_legitimo)

Bytes_hacker = base64.b64decode("eyJ1c3VhcmlvIjoiRG9uIFBlcGl0byBkZSBsb3MgcGFsb3RlcyIsInJvbCI6ImlzQWRtaW4iLCJpYXQiOjE2Njc5MzM1MzN9")
Body_hacker = Bytes_hacker.decode("utf-8")
print("El Body hackeado es:", Body_hacker)

#Validación JWT legítimo
Token_legitimo = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c3VhcmlvIjoiRG9uIFBlcGl0byBkZSBsb3MgcGFsb3RlcyIsInJvbCI6ImlzTm9ybWFsIiwiaWF0IjoxNjY3OTMzNTMzfQ.gfhw0dDxp6oixMLXXRP97W4TDTrv0y7B5YjD0U8ixrE"
Clave = "Con KeepCoding aprendemos"

try:
    decoded_token = jwt.decode(Token_legitimo, Clave, algorithms="HS256")
    print("JWT correcto")
    print("Body", decoded_token)
except jwt.InvalidTokenError:
    print("JWT no valido")    

#Intento de validar JWT hackeado
Token_hackeado = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c3VhcmlvIjoiRG9uIFBlcGl0byBkZSBsb3MgcGFsb3RlcyIsInJvbCI6ImlzQWRtaW4iLCJpYXQiOjE2Njc5MzM1MzN9.krgBkzCBQ5WZ8JnZHuRvmnAZdg4ZMeRNv2CIAODlHRI"
Clave_h = "Con KeepCoding aprendemos"


try:
    decoded_token_hack = jwt.decode(Token_hackeado, Clave_h, algorithms="HS256")
    print("JWT correcto")
    print("Body", decoded_token_hack)
except jwt.InvalidTokenError:
    print("JWT no valido")    