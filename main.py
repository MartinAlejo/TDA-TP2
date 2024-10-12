import csv
import sys
import os

sys.setrecursionlimit(30000)

# Dado un arreglo de monedas, devuelve el array excluyendo la moneda que tomo mateo
def decision_mateo(arr, inicio = 0, fin = 0):
    if arr[inicio] > arr[fin - 1]:
        return (inicio + 1, fin)
    return (inicio, fin - 1)

def _juego_monedas(arr, inicio = 0, fin = 0, memory = {}):
    if inicio >= fin:
        return 0
    
    key = (inicio, fin)
    if key in memory:
        return memory[key]

    primer_moneda = arr[inicio]
    ultima_moneda = arr[fin-1]
    
    decision_mateo_1 = decision_mateo(arr, inicio + 1, fin)
    decision_mateo_2 = decision_mateo(arr, inicio, fin-1)

    ganancia = max(primer_moneda + _juego_monedas(arr,decision_mateo_1[0],decision_mateo_1[1], memory), 
                   ultima_moneda + _juego_monedas(arr, decision_mateo_2[0], decision_mateo_2[1], memory))
    
    # guardamos la respuesta en la memoria
    memory[key] = ganancia

    return ganancia

# Dado un arreglo de monedas, devuelve la ganancia maxima de sofia
def juego_monedas(arr):
    memory = {}
    return _juego_monedas(arr, 0, len(arr), memory)

# Dado un archivo csv, devuelve una lista con las monedas
def obtener_monedas(path):
    with open(path, "r") as f:
        csv_reader = csv.reader(f, delimiter=";")
        return [int(moneda) for moneda in next(csv_reader)]

def main():
    ejemplos = [f for f in os.listdir("ejemplos") if f.endswith(".txt")]
    
    for ejemplo in sorted (ejemplos, key = lambda x: int(x.split(".")[0])):
        monedas = obtener_monedas(f"ejemplos/{ejemplo}")
        print(f"El resultado para {ejemplo} es: {juego_monedas(monedas)}")

if __name__ == "__main__":
    main()