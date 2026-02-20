listaNumero=[]
diccionario1={"suma":0,"promedio":0,"maximo":0,"minimo":0}
def analizar_lecturas(*numeros):
    contador=0
    for numero in numeros:
        try:
            numero=int(numero)
            if numero.is_integer():
                diccionario1["suma"]+=numero
                listaNumero.append(numero)
                listaNumero.sort()
                diccionario1.update({"maximo":listaNumero[-1]})
                diccionario1.update({"minimo":listaNumero[0]})
                #diccionario1.update({"promedio":numero/listaNumero.count()})
            if numero>100:
                contador=contador+1
                if contador>2:
                    raise ValueError("MAl FUNCIONAMIENTO DEL SENSOR")
        except ValueError:
            print("Dato omitido:tipo no valido")

    return diccionario1

print(analizar_lecturas(19,"error",2,4,1,))

# ==================== TODO FUNCIONA SOLO ME FALTA EL PROMEDIO ====================