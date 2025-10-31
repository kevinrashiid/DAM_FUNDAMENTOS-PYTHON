'''a=3
letra3="3"
print(a+a) ##operacion con numeros
print(letra3+letra3)'''
from turtle import st

##CASTEOS --> cambiar tipo
'''i= int(letra3)
print(letra3+letra3)
nombre=input("INGRESE SU NOMBRE")
print(nombre)'''

'''Buscar una posicion'''
fruta='manzana'

##print(fruta[len(fruta)-1])  ## a ##la ultima posicion
##print(len(fruta))  ## 7 ##numero total de caracteres
#def para definir funciones
'''for x in fruta:##BUCLE FOR
    print(x)'''

'''for i in fruta:
    print("\n",i,fruta)##m manzana'''


##BUCLE WHILE
'''indice=0
while indice < len(fruta):
    letra=fruta[indice]
    indice+=1 ##contador
    print(indice,letra)'''

contador=0
for i in fruta:
    if i=="a":
        contador+=1
print(contador)

##Rebanado de cadenas
s='ali'
print(s[0:1]) #a

#concatenacion
print("prueba "+s)

if fruta== "manzana":
    print("son iguales")


