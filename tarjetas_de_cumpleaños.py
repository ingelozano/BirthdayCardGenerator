#Libreria PIL para trabajar con imagenes
from PIL import Image, ImageDraw, ImageFont
#Libreria os para trabajar con rutas de archivos
import os

#Esta función es la encarganda de generar la tajerta de cumpleaños con la información dada
def generar_tarjeta(nombre, edad, mensaje, imagen_fondo):
    # Crear un objeto ImageDraw para dibujar sobre la imagen
    draw = ImageDraw.Draw(imagen_fondo)
    
    # Cargar una fuente llamativa (asegúrate de tener "impact.ttf" en el mismo directorio que el script)
    font = ImageFont.truetype("impact.ttf", 60)
    
    # Agregar texto personalizado a la imagen con un salto de línea en el mensaje
    text = f"Feliz cumpleaños, {nombre}!\nHoy cumples {edad} años.\n\n{mensaje}"
    
    # Centrar el texto en la imagen
    text_width, text_height = draw.textsize(text, font=font)
    image_width, image_height = imagen_fondo.size
    x = (image_width - text_width) // 2
    y = (image_height - text_height) // 2
    
    draw.text((x, y), text, fill=(0, 0, 0), font=font)  # Letras negras (RGB: 0, 0, 0)

    # Guardar la tarjeta en un archivo
    imagen_fondo.save("tarjeta_personalizada.png")

# Obtener información del destinatario desde el usuario
nombre = input("Ingresa el nombre del destinatario: ")
edad = input("Ingresa la edad del destinatario: ")
mensaje = input("Ingresa el mensaje de cumpleaños: ")

# Obtener la ruta completa del archivo "fondo.jpg" (asegúrate de que esté en el mismo directorio que el script)
directorio_actual = os.path.dirname(os.path.abspath(__file__))
ruta_fondo = os.path.join(directorio_actual, "fondo.jpg")

# Cargar la imagen de fondo
imagen_fondo = Image.open(ruta_fondo)

# Generar la tarjeta con la información proporcionada
generar_tarjeta(nombre, edad, mensaje, imagen_fondo)

print("Tarjeta generada exitosamente. ¡Feliz cumpleaños!")
