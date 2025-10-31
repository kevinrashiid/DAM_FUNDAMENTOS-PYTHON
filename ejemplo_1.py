#print('Hola Martin')

a = 0 # Numero entero
b = 0.0 # Numero decimal (Real o float)
c = 2 + 4j #complejo
d = 1.2e-3 # notación científica: 0,0012

a += 1 # Esto es lo mismo que a++ en Java
b -= 0.5 # Esto para reducir

#print(a)
#print(b)

#print(a,b,c,d,sep=',',end='+')
#print('prueba')

#print(a+b)

cadena = "Prueba de."
#         0123456789
cadena_simple = 'Prueba de cadena\' simple.' # Si quieres poner comillas dentro puedes poner un \ delante de las comillas

#print(cadena_simple)
#print(cadena + ' ' + cadena_simple)

#print(a + len(cadena)) # Esto contea el número de carácteres
#print(str(a) + cadena) # Esto sería el metodo efectivo

#print(a*cadena) # Esto duplica la respuesta, por lo cual se duplicaria la cadena por el numero que hay en A

#print(cadena[5]) # Esto muestra el char que hay en esa frase, mirar arriba para ver y
#print(cadena[-1]) # -1 equivale a decir que meustre el último
#print(cadena[3:]) # esto significa que s ecome las tres primeras letras
#print(cadena[:3]) # esto es que muestra los 3 primeros
#print('texto añadido')

#n_1 = 5
#n_2 = 6
#n_1 + n_2
#total = n_1 + n_2
#print(total)
#total_divmod = n_2 / n_1
#print(total_divmod)
# cont += 1        Esto es un contador de toda la vida
#b1 = 3 & 2
#b2 = 3 >> 1
#print(b1)
#print(b2)
#numCient = 1.5e-3 # para marcar un exponenete sobre 10 se pone ...e-X
#print(numCient)
#print('abcde' [-1]) # lo mismo que en java
#cadena = 'inmutable'
#cadena = "n" + cadena[1:]
#print(cadena)



# Esto son cosas sobre sumas completas en vez de juntar
# Tambien el mitico Scanner
'''i = "3"
i = int(i)
print(i+i)
nombre = input('Igrese su ¯nombre: ') # Esto es lo mismo que un Scanenr
print(nombre) '''

fruta = 'manzana'
letra = fruta[-2]
#print(letra)
# para hacer un /* */ de java es necesario 3 comillas simples para abrir y cerrar
'''x = 3
w = fruta[x - 1]
print(w)
print(fruta[len(fruta)-4])
'''
'''indice = 0

while indice < len(fruta):
    letra = fruta[indice]
    print(indice, letra)
    indice += 1'''
# indice = 0 # esto se puede usar para una especie de contador
'''for letra in fruta:
    #print("\n")
    print("\n",indice, letra)
    indice += 1 # esto es como un ++ en java
'''
'''for letra in fruta:  # Esto es para mostrar el numero de veces que aparece un caracter
    if letra == 'a':  # esto es un operador logico
        indice = indice + 1
print(indice)
'''

s = 'Monty Python'
#print(s[:4])  # Tambien se puede hacer [0:4]
# Esto da Month
#print(s[6:7])
# Esto P
#print(s[6:20])
# Esto Python

#print('Buenas ' + s)

#print('M' in s)  # el IN es una manera para buscar algo en una cadena
'''fruta = 'manzana'
if fruta == 'manzana':
    print('Palabra encontrada!')
'''

'''saludo = 'Hola Bob'
zap = saludo.lower()
print(zap)
'''

'''fruta = 'banana'
pos = fruta.find('an')
print(pos)'''

palabra = 'manzana'
print(palabra.find('na'))

