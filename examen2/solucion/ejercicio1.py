
def limpiarInvetario(lista_datos):
    respuesta = {}
    for producto in lista_datos:
        respuesta.update({producto["id"]:{producto["nombre"]:producto["precio"]}})
        return respuesta


def filtrar_precio_entre(productos,minimo=0,maximo=80000):
    resultado=[]
    for id,producto in productos.items():
        tupla=(producto.keys(),producto.values())
        resultado.append()
    return resultado

inventario = [
    {"id": 101,"nombre": "Laptop Pro 16","precio": 1450.00,"stock": 5},
    {"id": 102, "nombre": "Ratón Inalámbrico", "precio": 25.99, "stock": 50},
    {"id": 103, "nombre": "Monitor 4K 27", "precio": 380.50, "stock": 12},
    {"id": 104, "nombre": "Smartphone Alpha", "precio": 899.00, "stock": 8},
    {"id": 105, "nombre": "Teclado Mecánico RGB", "precio": 120.00, "stock": 20},
    {"id": 106, "nombre": "Tarjeta Gráfica RTX", "precio": 650.00, "stock": 4},
    {"id": 107, "nombre": "Auriculares Noise Cancelling", "precio": 210.00, "stock": 15},
    {"id": 108, "nombre": "Servidor NAS", "precio": 520.00, "stock": 2}
]


print(inventario)

diccionario_comprimido=limpiarInvetario(inventario)
print(diccionario_comprimido)
print(filtrar_precio_entre(diccionario_comprimido))
print(filtrar_precio_entre(diccionario_comprimido,maximo=200))

print(filtrar_precio_entre(diccionario_comprimido,minimo=600))

print(filtrar_precio_entre(diccionario_comprimido,maximo=8000))


