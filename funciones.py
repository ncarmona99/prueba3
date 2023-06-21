#Funciones

#Función imprimir menú

nombreDueno = None

def imprimirMenu():
    print("*****************************************")
    print('Menú de sistema automotora "Auto Seguro"')
    print("*****************************************")
    print()
    print("1. Grabar")
    print("2. Buscar")
    print("3. Imprimir certificados")
    print("4. Salir")
def despedida(nombre):
    print("Adios",nombre)
    if nombreDueno == None:
        print("Adios")
    else:
        print("Adios", nombreDueno)