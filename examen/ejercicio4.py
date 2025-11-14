import random

aleatorio=random.randint(5000000, 20000000)
bandera=True
while bandera:
    aleatorio = random.randint(5000000, 20000000)  ##numero aletorio con notacion cientifica
    for i in range(2, int(aleatorio / 2)):
        if aleatorio%i!=0:
            bandera=False
print(aleatorio)

#5000000, 20000000

