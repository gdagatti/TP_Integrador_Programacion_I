def ordenamiento_insercion(lista):
    # Recorre la lista desde el segundo elemento hasta el final
    for i in range(1, len(lista)):
        indice = lista[i]  # Elemento actual a insertar
        j = i - 1  # Índice del elemento anterior

        # Mover elementos mayores que el índice hacia la derecha
        while j >= 0 and indice < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1

        # Insertar índice en su posición correcta
        lista[j + 1] = indice
    return lista

# Ejemplo de uso
if __name__ == "__main__":
    lista = [12, 11, 13, 5, 6]
    print("Lista original:", lista)
    lista_ordenada = ordenamiento_insercion(lista)
    print("Lista ordenada:", lista_ordenada)
