# Archivos [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con archivos

import csv


def ej3():
    print('Ejercicio de archivos CSV 1º')
    archivo = 'stock.csv'
    
    # Realice un programa que abra el archivo 'stock.csv'
    # en modo lectura y cuente el stock total de tornillos
    # a lo largo de todo el archivo, 
    # sumando el stock en cada fila del archivo

    # Para eso debe leer los datos del archivo
    # con "csv.DictReader", y luego recorrer los datos
    # dentro de un bucle y solo acceder a la columna "tornillos"
    # para cumplir con el enunciado del ejercicio

    # Comenzar aquí, recuerde el identado dentro de esta funcion
    
    total_tornillos = 0
    with open('stock.csv') as archivo:
        stock = list(csv.DictReader(archivo))
        for fila in stock:
            tornillos = fila.get('tornillos')
            total_tornillos = total_tornillos + int(tornillos)
            print(fila)
            print("La cantidad de tornillos es: ",tornillos)
        print("El total de tornillos es: ",total_tornillos)
            
        
        



def ej4():
    print('Ejercicios con archivos CSV 2º')
    archivo = 'propiedades.csv'

    # Realice un programa que abra el archivo CSV "propiedades.csv"
    # en modo lectura. Recorrar dicho archivo y contar
    # la cantidad de departamentos de 2 ambientes y la cantidad
    # de departamentos de 3 ambientes disponibles.
    # Al finalizar el proceso, imprima en pantalla los resultados.

    # Tener cuidado que hay departamentos que no tienen definidos
    # la cantidad de ambientes, verifique el texto no esté vacio
    # antes de convertirlo a entero con "int( .. )"
    # NOTA: Si desea investigar puede evitar que el programa explote
    # utilizando "try except", tema que se verá la clase que viene.

    # Comenzar aquí, recuerde el identado dentro de esta funcion
    deptos_2amb = 0
    deptos_3amb = 0
    with open('propiedades.csv') as archivo:
        propiedades = list(csv.DictReader(archivo))
        cantidad_filas = len(propiedades)
        
        for i in range(cantidad_filas):
        
            depto = propiedades[i]
            try:
                ambientes = int(depto.get('ambientes'))
                print('Depto', i, 'ambientes:', ambientes)
            except:
                print('Error Fila', i, 'dato faltante')
            if ambientes == 2:
                deptos_2amb += ambientes 
            elif ambientes == 3:
                deptos_3amb += ambientes
    
    print("La cantidad de deptos 2 amb son: ",deptos_2amb)
    print("La cantidad de deptos 3 amb son: ",deptos_3amb)   

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej3()
    ej4()
