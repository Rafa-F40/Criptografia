#XOR de datos binarios
def xor_data(binary_data_1, binary_data_2):
    return bytes([b1 ^ b2 for b1, b2 in zip(binary_data_1, binary_data_2)])


Clave_Fija=0xB1EF2ACFE2BAEEFF
Clave_Final=0x91BA13BA21AABB12
Properties=(hex(Clave_Fija^Clave_Final))
print(Properties[2:])

Clave_Fija=0xB1EF2ACFE2BAEEFF
Clave_Produccion=0xB98A15BA31AEBB3F
Dinamica=(hex(Clave_Fija^Clave_Produccion))
print(Dinamica[2:])