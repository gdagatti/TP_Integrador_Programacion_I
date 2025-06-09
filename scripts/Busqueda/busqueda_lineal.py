# Definición de la función 
def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i  # Retorna la posición del elemento
    return -1  # Retorna -1 si el elemento no se encuentra

# Ejemplo de uso
if __name__ =="__main__":
    lista = [3, 5, 2, 8, 1, 9]
    objetivo = 8
    posicion = busqueda_lineal(lista, objetivo)
    if posicion != -1:
        print(f"El elemento {objetivo} se encuentra en la posición {posicion}.")
    else:
        print(f"El elemento {objetivo} no se encuentra en la lista.")
