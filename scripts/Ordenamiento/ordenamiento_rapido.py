def ordenamiento_rapido(lista):
    if len(lista) <= 1:
        return lista  # Una lista de un elemento o menos ya está ordenada

    # Seleccionar el pivote (en este caso, el último elemento)
    pivote = lista[-1]
    menores = []
    mayores = []
    iguales = []

    # Particionar la lista
    for x in lista:
        if x < pivote:
            menores.append(x)
        elif x > pivote:
            mayores.append(x)
        else:
            iguales.append(x)

    # Aplicar Ordenamiento rápido recursivamente a las sub-listas
    return ordenamiento_rapido(menores) + iguales + ordenamiento_rapido(mayores)

# Ejemplo de uso
if __name__ == "__main__":
    lista = [3, 6, 8, 10, 1, 2, 1]
    print("Lista original:", lista)
    lista_ordenada = ordenamiento_rapido(lista)
    print("Lista ordenada:", lista_ordenada)
