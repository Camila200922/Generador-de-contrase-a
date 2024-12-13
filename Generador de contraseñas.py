import random
caracteres= "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
longuitud = int(input("Introdusaca la longuitud de su contraseña"))

contraseña= ""
for  i in range (longuitud):
    contraseña += random.choice(caracteres)

print(contraseña)