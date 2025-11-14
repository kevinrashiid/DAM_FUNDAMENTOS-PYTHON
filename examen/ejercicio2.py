
palabra=str(input("INTRODUCE EL MENSAJE-> "))
cifra=int(input("INTRODUCE LA CIFRA -> "))

palabra=palabra[::-1]#al revés
print(palabra)
cifraTexto=str(cifra)
palabra=palabra.lower()
nueva=""
for i in palabra:
    if i=="a":
        palabra=palabra.replace("a",cifraTexto)
    if i=="e":
        palabra=palabra.replace("e",cifraTexto)
    if i == "i":
        palabra = palabra.replace("i", cifraTexto)
    if i == "o":
        palabra = palabra.replace("o", cifraTexto)
    if i == "u":
        palabra = palabra.replace("u", cifraTexto)
'''for i in palabra:
    if i=='a' or i=="e" or i=="i" or i=="o" or i=="e":
        nueva=palabra.replace(i,cifraTexto)'''
print(palabra)

#palabra separada

#nueva.find(cifra)
##apartir de la cifra(utilizada como indice) la partas en dos