
#PRIMER PASO ACABADO
frase=str(input("LA FRASE ES -> "))
letra=str(input("LA LETRA ES --> "))
bandera=False

for i in frase:
    if i==" ":
        frase=frase.replace(i," ")
    elif letra!=i:
        frase=frase.replace(i,"*")

print(frase)