import qrcode
from tkinter import Tk, Label, Entry, Button, StringVar
from tkinter.filedialog import asksaveasfilename

# Función que genera el QR y permite guardarlo
def generar_qr():
    ssid = ssid_var.get()  # Obtener el nombre de la red desde la ventana emergente
    password = password_var.get()  # Obtener la contraseña desde la ventana emergente
    encryption_type = "WPA"  # Puedes cambiar esto si usas WEP o una red sin contraseña ("nopass")
    
    # Crear el string del QR
    wifi_data = f"WIFI:T:{encryption_type};S:{ssid};P:{password};;"

    # Generar el código QR
    qr = qrcode.QRCode(
        version=1,  # Tamaño del QR (1 es el más pequeño)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Nivel de corrección de errores
        box_size=10,  # Tamaño de los cuadrados del QR
        border=4  # Tamaño del borde
    )

    qr.add_data(wifi_data)
    qr.make(fit=True)

    # Crear imagen del QR
    img = qr.make_image(fill='black', back_color='white')

    # Ventana emergente para seleccionar dónde guardar el archivo
    ruta_guardado = asksaveasfilename(
        defaultextension=".png",  # Extensión por defecto
        filetypes=[("PNG files", "*.png")],  # Tipos de archivos permitidos
        title="Guardar imagen del QR"
    )

    # Si se selecciona una ruta, guardar la imagen
    if ruta_guardado:
        img.save(ruta_guardado)
        print(f"Imagen guardada correctamente en {ruta_guardado}")
    else:
        print("No se seleccionó ninguna ruta.")

# Configurar la ventana emergente
root = Tk()
root.title("Datos de la red Wi-Fi")

# Variables para almacenar el nombre de la red y la contraseña
ssid_var = StringVar()
password_var = StringVar()

# Etiquetas y campos de entrada
Label(root, text="Nombre de la red Wi-Fi (SSID):").grid(row=0, column=0, padx=10, pady=10)
Entry(root, textvariable=ssid_var).grid(row=0, column=1, padx=10, pady=10)

Label(root, text="Contraseña de la red Wi-Fi:").grid(row=1, column=0, padx=10, pady=10)
Entry(root, textvariable=password_var, show="*").grid(row=1, column=1, padx=10, pady=10)

# Botón para generar el código QR
Button(root, text="Generar QR", command=generar_qr).grid(row=2, column=0, columnspan=2, pady=20)

# Iniciar la ventana
root.mainloop()