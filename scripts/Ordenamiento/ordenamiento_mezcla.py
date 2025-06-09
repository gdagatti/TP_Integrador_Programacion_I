def ordenamiento_mezcla(lista):
    if len(lista) <= 1:
        return lista  # Una lista de un elemento o menos ya está ordenada

    # Dividir la lista en dos mitades
    medio = len(lista) // 2
    izquierda = lista[:medio]
    derecha = lista[medio:]

    # Llamar recursivamente al ordenamiento_mezcla para ambas mitades
    izquierda = ordenamiento_mezcla(izquierda)
    derecha = ordenamiento_mezcla(derecha)

    # Mezclar las dos mitades ordenadas
    return mezclar(izquierda, derecha)

def mezclar(izquierda, derecha):
    resultado = []
    i = j = 0

    # Comparar elementos de ambas listas y añadir el menor al resultado
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    # Agregar los elementos restantes de la lista izquierda, si los hay
    while i < len(izquierda):
        resultado.append(izquierda[i])
        i += 1

    # Agregar los elementos restantes de la lista derecha, si los hay
    while j < len(derecha):
        resultado.append(derecha[j])
        j += 1

    return resultado

# Ejemplo de uso
if __name__ == "__main__":
    lista = [38, 27, 43, 3, 9, 82, 10]
    print("Lista original:", lista)
    lista_ordenada = ordenamiento_mezcla(lista)
    print("Lista ordenada:", lista_ordenada)
