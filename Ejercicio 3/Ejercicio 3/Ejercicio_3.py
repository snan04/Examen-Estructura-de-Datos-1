import tkinter as tk

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        max_idx = i
        for j in range(i+1, n):
            if arr[j] > arr[max_idx]:
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
    return arr

def get_input():
    input_arr = []
    while True:
        num = int(input("Ingrese un numero (0 para detener): "))
        if num == 0:
            break
        input_arr.append(num)
    return input_arr

def main():
    input_arr = get_input()
    size = len(input_arr)
    avg = sum(input_arr) / size
    sorted_arr = selection_sort(input_arr)
    total_sum = sum(sorted_arr)

    print(f"Tamano del arreglo: {size}")
    print(f"Promedio del arreglo: {avg}")
    print(f"Suma del arreglo: {total_sum}")
    print(f"Ordenamiento de mayor a menor: {sorted_arr}")

if __name__ == "__main__":
    main()
