def ordenamiento_burbuja(lista):
    n = len(lista)
    for i in range(n):
        # Para detectar si se realizaron intercambios en esta pasada
        intercambio = False
        for j in range(0, n - i - 1):
            # Comparar el elemento actual con el siguiente
            if lista[j] > lista[j + 1]:
                # Intercambiar los elementos
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambio = True
        # Si no se realizaron intercambios, la lista ya está ordenada
        if not intercambio:
            break
    return lista

# Ejemplo de uso
if __name__ == "__main__":
    lista = [64, 34, 25, 12, 22, 11, 90]
    print("Lista original:", lista)
    lista_ordenada = ordenamiento_burbuja(lista)
    print("Lista ordenada:", lista_ordenada)