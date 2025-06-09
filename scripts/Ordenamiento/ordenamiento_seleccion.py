def ordenamiento_seleccion(lista):
    n = len(lista)
    for i in range(n):
        # Encontrar el índice del elemento mínimo en la parte no ordenada
        min = i
        for j in range(i + 1, n):
            if lista[j] < lista[min]:
                min = j
        
        # Intercambiar el elemento mínimo encontrado con el primer elemento de la parte no ordenada
        lista[i], lista[min] = lista[min], lista[i]
    
    return lista

# Ejemplo de uso
if __name__ == "__main__":
    lista = [64, 25, 12, 22, 11]
    print("Lista original:", lista)
    lista_ordenada = ordenamiento_seleccion(lista)
    print("Lista ordenada:", lista_ordenada)