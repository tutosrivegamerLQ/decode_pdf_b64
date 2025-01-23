import base64
import time
import os

def decode_pdf(str_code, number_factus):
    # Ruta para guardar el archivo PDF decodificado
    ruta_pdf_salida = f"./files/factura_{number_factus}.pdf"
    # Decodificar el contenido base64
    contenido_pdf = base64.b64decode(str_code)
    # Guardar el contenido decodificado como un archivo PDF
    with open(ruta_pdf_salida, "wb") as archivo_pdf:
        archivo_pdf.write(contenido_pdf)
    print(f"El archivo PDF se ha decodificado y guardado como: {ruta_pdf_salida}")
    return ruta_pdf_salida.replace('./files/', '')

def remove_file(path):
    os.remove(f'./files/{path}')


