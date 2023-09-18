# Crear una matriz de 3x3 (3 filas y 3 columnas)
matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

# Acceder a un elemento específico
elemento = matriz[1][2]  # Esto accede al elemento en la fila 1 (segunda fila) y columna 2 (tercera columna)
print("Elemento en la fila 1, columna 2:", elemento)  # Imprimirá 6

# Recorrer la matriz y mostrar sus elementos
print("Elementos de la matriz:")
for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ")  # Imprime los elementos en la misma fila
    print()  # Salto de línea para pasar a la siguiente fila

# Modificar un elemento
matriz[0][0] = 0  # Cambiar el valor en la fila 0 y columna 0 a 0

# Mostrar la matriz actualizada
print("Matriz actualizada:")
for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ")
    print()



# Crear una matriz tridimensional de 2x3x4

#Primera matriz:
arreglo_3d = [[[1, 2, 3, 4],
               [5, 6, 7, 8],
               [9, 10, 11, 12]],
#Segunda matriz:
              [[13, 14, 15, 16],
               [17, 18, 19, 20],
               [21, 22, 23, 24]]]

# Acceder a un elemento específico
elemento = arreglo_3d[1][2][3]  # Acceder al elemento en la segunda matriz, tercera fila y cuarta columna
print("Elemento:", elemento)  # Imprimirá 24
