#Sistema Auto Seguro

acum = 0
nombreDueno = None

import funciones as fn

try:

    while True:

        fn.imprimirMenu()

        op = int(input("\nIngrese el número de opción deseada:"))

        if op == 1:
            datos = []
            tipo = input("Ingrese el tipo de patente: ")
            datos.append(tipo)
            while True:
                patente = input("Ingrese la patente del vehículo: ")
                if len(patente) != 6:
                    print("Los datos de la patente no son correctos, reintente.") 
                else:
                    datos.append(patente)
                    break
            marca = input("Ingrese la marca del vehículo: ")
            while True:
                if len(marca) < 2 and len(marca) > 15:
                    print("La longitud de la marca ingresada no es válida, debe tener entre 2 y 15 caractéres")
                else:
                    datos.append(marca)
                    break
            precio = int(input("Ingrese el precio: "))
            while True:
                if precio < 5000000:
                    print("El precio ingresado no es válido. El monto debe ser mayor a $5.000.000")
                else:
                    datos.append(precio)
                    break
            montoMulta = input("Ingrese el monto de multa, si no tiene, ingrese 0: ")
            datos.append(montoMulta)
            fechaMulta = input("Ingrese fecha de la multa (dd/mm/aa), si no tiene, ingrese 0: ")
            datos.append(fechaMulta)
            fechaRegistro = input("Ingrese la fecha del registro del vehículo (dd/mm/aa): ")
            datos.append(fechaRegistro)
            nombreDueno = input("Ingrese el nombre del dueño: ")
            datos.append(nombreDueno)
            input("Datos guardados con éxito, ingrese cualquier tecla para continuar: ")
        elif op == 2:
            pat = input("Ingrese la patente del vehículo que quiere buscar: ")
            print(pat)
            print(datos[1])
            if pat == datos[1]:
                print("La patente es: ", pat)
                print("El tipo de patente es: ", datos[0])
                print("La marca del vehículo es: ", datos[2])
                print("El precio del vehículo es: ", datos[3])
                print("El monto de la multa es: ", datos[4])
                print("La fecha de la multa es: ", datos[5])
                print("La fecha de registro es: ", datos[6])
                print("El nombre del dueño es: ", datos[7])
                input("Ingrese cualquier tecla para continuar: ")
            else:
                print("La patente ingresada no es válida o no existe en los registros")
        elif op == 3:
            int(input(""))
            print("Certificado impreso con éxito")
        elif op == 4:
            fn.despedida(nombreDueno)
            break
        else:
            print("El número ingresado no es válido, reintente")
except:
    print("ERROR: problema en los datos ingresados")