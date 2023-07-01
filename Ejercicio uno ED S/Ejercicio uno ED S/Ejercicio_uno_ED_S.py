import tkinter as tk

def search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

def enter_items():
    items = []
    while True:
        item = int(input("Ingrese un numero (0 para salir): "))
        if item == 0:
            break
        items.append(item)
    print("Arreglo: ", items)
    x = int(input("Ingrese el elemento que desea buscar: "))
    result = search(items, x)
    if result == -1:
        print("Elemento no encontrado")
    else:
        print("Elemento encontrado en el indice:", result)

if __name__ == "__main__":
    enter_items()
