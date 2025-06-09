def busqueda_binaria(lista, objetivo):
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio  # Retorna la posición del elemento
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1  # Retorna -1 si el elemento no se encuentra

# Ejemplo de uso
if __name__ =="__main__":
    lista_ordenada = [1, 2, 3, 5, 8, 9]
    objetivo = 5
    posicion = busqueda_binaria(lista_ordenada, objetivo)
    if posicion != -1:
        print(f"El elemento {objetivo} se encuentra en la posición {posicion}.")
    else:
        print(f"El elemento {objetivo} no se encuentra en la lista.")
