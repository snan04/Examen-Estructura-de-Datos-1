import tkinter as tk

class App:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Ordenamiento Burbuja")
        self.window.geometry("400x400")

        self.label = tk.Label(self.window, text="Ingrese los elementos separados por coma:")
        self.label.pack()

        self.entry = tk.Entry(self.window)
        self.entry.pack()

        self.button_add = tk.Button(self.window, text="Agregar", command=self.add_elements)
        self.button_add.pack()

        self.button_sort = tk.Button(self.window, text="Ordenar", command=self.sort_elements)
        self.button_sort.pack()

        self.label_size = tk.Label(self.window, text="Tamano del arreglo: ")
        self.label_size.pack()

        self.label_max = tk.Label(self.window, text="Elemento de mayor valor: ")
        self.label_max.pack()

        self.label_min = tk.Label(self.window, text="Elemento de menor valor: ")
        self.label_min.pack()

        self.elements = []

    def add_elements(self):
        elements = [int(e) for e in self.entry.get().split(",")]
        for e in elements:
            if e != 0:
                self.elements.append(e)
            else:
                break

    def sort_elements(self):
        n = len(self.elements)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.elements[j] > self.elements[j+1]:
                    self.elements[j], self.elements[j+1] = self.elements[j+1], self.elements[j]

        size = len(self.elements)
        max_element = max(self.elements)
        min_element = min(self.elements)

        self.label_size.config(text=f"Tamano del arreglo: {size}")
        self.label_max.config(text=f"Elemento de mayor valor: {max_element}")
        self.label_min.config(text=f"Elemento de menor valor: {min_element}")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()

