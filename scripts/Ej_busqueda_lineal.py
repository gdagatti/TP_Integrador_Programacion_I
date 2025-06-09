import busqueda_lineal as bl

lista = [4, 2, 7, 1, 9, 3]
objetivo = 7
resultado = bl.busqueda_lineal(lista, objetivo)
    
if resultado != -1:
    print(f"El elemento {objetivo} se encuentra en la posición {resultado}.")
else:
    print(f"El elemento {objetivo} no se encuentra en la lista.")
