import os

def buscar_palabra_en_archivos(palabra, directorio):
    archivos_con_palabra = []
    # Iterar sobre todos los archivos en el directorio
    for archivo in os.listdir(directorio):
        if archivo.endswith(".txt"):
            # Abrir el archivo y buscar la palabra
            with open(os.path.join(directorio, archivo), 'r', encoding='utf-8') as file:
                contenido = file.read()
                if palabra in contenido:
                    archivos_con_palabra.append(archivo)
    return archivos_con_palabra

# Pedir al usuario la palabra a buscar y el directorio
palabra_a_buscar = input("geovanny")
directorio_a_buscar = r"C:\RecuperacionInformacion" 

# Llamar a la función y mostrar los resultados
archivos_encontrados = buscar_palabra_en_archivos(palabra_a_buscar, directorio_a_buscar)
if archivos_encontrados:
    print("La palabra '{}' se encontro en los siguientes archivos:".format(palabra_a_buscar))
    for archivo in archivos_encontrados:
        print(archivo)
else:
    print("La palabra '{}' no se encontro en ningun archivo en el directorio especificado.".format(palabra_a_buscar))