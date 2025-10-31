from jeepney.low_level import Boolean

print("Hola felix")
a=0.2 #realo float
b=5 #Entero
e=1.2e-3 #notacion cientifica : 00.012
a+=1#incremento
b-=0.5#decremento


print(a)

print(a,b,e,a,b,sep=("/")) ##imprimimos definimos la separacion que sea /

print(a,b,e,a,b,sep="/", end=" ")
print("prueba")
print (a+b)
cadena="Prueba de cadena"#comillas dobles
cadena_simple= 'prueba de cade simple' #comillas simples
cadena_signo= 'prueba de cade \' simple' #con \ ignora el caracte y no lo representa como separador de texto
print (cadena_simple , cadena_signo) #concatena con ,
print (cadena_simple + cadena_signo)#concatena con +

print (str(a)+cadena)
#print (a+cadena)#ERROR

print(len(cadena))#suelta la longitud de la cadena

#print(b*cadena_simple)#esto se podria hacer pero me da error


print (cadena[2])#la segunda posicion
print (cadena[-1])#la ultima posicion

print(cadena[3:7]) #muestra las posiciones 3 y 7 pero ellas no incluidas

#cadena[5]="k"#por ejemplo esto no se puede hacer



#solo existen 3 tipos de objetos/variables
#numeros
#caracteres
#booleanos
#sumas
numero1=5
numero2=3
print( numero1+numero2)

b1=3>>6
#print(b1)

cadena='hola hola'
print(cadena.upper())
##prueba CODIGO SUBIDO


