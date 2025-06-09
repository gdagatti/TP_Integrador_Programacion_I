import busqueda_binaria as bb

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
objetivo = 7
resultado = bb.busqueda_binaria(lista, objetivo)
    
if resultado != -1:
    print(f"El elemento {objetivo} se encuentra en la posición {resultado}.")
else:
    print(f"El elemento {objetivo} no se encuentra en la lista.")
