
##DICCIONARIO
tienda={
    "patata":3,
    "lentejas":4,
    "melon":5,
    "garbanzos":5
}

##SORTED siempre recibe un array diccionario etc
###ordena tienda por valor
sorted(tienda.items(),key=lambda items:items[1],reverse=True)
