

def convertir_a_entero(lista=[]):#RECIBE UNA LISTA
    resultado=[]
    for item in lista:
        try:
            numero=int(item)
            resultado.append(numero)
        except ValueError:
            pass #si salta la excepsion la pasa al siguiente item
    return resultado


lista_entrada=["10", "hola", "20", "3.5"]
print(lista_entrada)

lista_numeros=convertir_a_entero(lista_entrada)
print(lista_numeros)
