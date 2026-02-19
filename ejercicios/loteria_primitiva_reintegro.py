
'''5. Una lotería primitiva, por si no lo sabes, está formada por seis números y otro adicional
para el reintegro. Los seis primeros números están comprendidos entre el 1 y el 49
(ambos inclusive) que no pueden estar repetidos. El reintegro es un número entre el 0 y
el 9. Haced un programa en python que calcule una combinación de números de forma
aleatoria para la primitiva cumpliendo las normas explicadas antes y que luego la
muestre por pantalla ordenada de menor a mayor. Lógicamente, también debería de
mostrar el complementario.'''
import random
primitiva=[]
while len(primitiva)<7:
    azar=random.randint(1,49)
    ###en caso de que el azar de 0 es decir no esta en la lista
    ### añade el numero en la lista
    if primitiva.count(azar)==0:
        primitiva.append(azar)
reintegro=random.randint(1,9)
primitiva.append(reintegro)
print(primitiva)
