def pvp(precio, iva):
    # Convertimos el IVA a porcentaje (por ejemplo 21 pasa a 0.21)
    iva_decimal = iva / 100

    # Calculamos el precio final sumando el IVA
    precio_final = precio + (precio * iva_decimal)

    # Redondeamos el resultado a 2 decimales
    return round(precio_final, 2)

print(pvp(14, 0))
print(pvp(34.4, 21))