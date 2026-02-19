lista=[2,3,4,4,5,4,6,7,8]
numero=(input("SI TU NUMERO NO ESTA EN LA LISTA LO AÑADO"))
if numero.isdigit():
    numero=int(numero)
    while lista.count(numero)>0:###count cuenta cuantas veces aparece el numero
        ###si es mayor que 0 lo elimana
        lista.remove(numero)
    print(lista)
else:
    print("INTRODUCE UN ENTERO")