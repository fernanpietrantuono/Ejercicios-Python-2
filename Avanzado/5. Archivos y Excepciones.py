try:
    with open('archivo_inexistente.txt', 'r') as archivo:
        contenido = archivo.read()
        print(contenido)
except FileNotFoundError:
    print("\033[91mArchivo no encontrado\033[0m")
