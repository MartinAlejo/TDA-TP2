import csv
import sys
import os

sys.setrecursionlimit(30000)

# Dado un arreglo de monedas, devuelve una tupla, que contiene los indices
# del array excluyendo la moneda que tomo Mateo
def decision_mateo(arr, inicio = 0, fin = 0):
    if arr[inicio] > arr[fin - 1]:
        return (inicio + 1, fin)
    return (inicio, fin - 1)

def _juego_monedas(arr, inicio = 0, fin = 0, memory = {}):
    if inicio >= fin:
        return 0
    
    key = (inicio, fin)
    if key in memory:
        return memory[key] # El subproblema ya fue resuelto

    primer_moneda = arr[inicio]
    ultima_moneda = arr[fin-1]
    
    decision_mateo_1 = decision_mateo(arr, inicio + 1, fin)
    decision_mateo_2 = decision_mateo(arr, inicio, fin-1)

    ganancia = max(primer_moneda + _juego_monedas(arr,decision_mateo_1[0],decision_mateo_1[1], memory), 
                   ultima_moneda + _juego_monedas(arr, decision_mateo_2[0], decision_mateo_2[1], memory))
    
    # Guardamos la ganancia en la memoria
    memory[key] = ganancia

    return ganancia

# Dado un arreglo de monedas, devuelve la ganancia maxima de Sophia y la memoria que contiene la  
# solucion de cada subproblema
def juego_monedas(arr):
    memory = {}
    return _juego_monedas(arr, 0, len(arr), memory), memory

# Dado un archivo csv, devuelve una lista con las monedas
def obtener_monedas(path):
    with open(path, "r") as f:
        csv_reader = csv.reader(f, delimiter=";")
        return [int(moneda) for moneda in next(csv_reader)]

# Dado la memoria de llamadas recursivas y el arreglo de monedas, reconstruye el camino de las 
# decisiones tomadas, junto con la ganancia de Mateo.
def reconstruir_solucion(memory, arr):
    solucion = []
    inicio = 0
    fin = len(arr)
    ganancia_mateo = 0

    def calcular_decision_mateo(inicio, fin):
        # Caso base
        if inicio >= fin:
            return 0
        if arr[inicio] > arr[fin - 1]:
            solucion.append(f'Mateo agarra la primera ({arr[inicio]})')
            return arr[inicio]
        else:
            solucion.append(f'Mateo agarra la ultima ({arr[fin-1]})')
            return arr[fin-1]

    while inicio < fin:
        decision_mateo_1 = decision_mateo(arr, inicio + 1, fin) # En este caso, Mate agarro la primera
        decision_mateo_2 = decision_mateo(arr, inicio, fin-1) # En este caso, Mate agarro la ultima

        if memory[(inicio, fin)] == arr[inicio] + memory.get((decision_mateo_1[0], decision_mateo_1[1]), 0):
            solucion.append(f'Sophia debe agarrar la primera ({arr[inicio]})')
            ganancia_mateo += calcular_decision_mateo(inicio+1, fin)
            inicio = decision_mateo_1[0]
            fin = decision_mateo_1[1]
        else:
            solucion.append(f'Sophia debe agarrar la ultima ({arr[fin-1]})')
            ganancia_mateo += calcular_decision_mateo(inicio, fin-1)
            inicio = decision_mateo_2[0]
            fin = decision_mateo_2[1]

    return solucion, ganancia_mateo

def main(path):

    monedas = obtener_monedas(path)
    resultado, memoria = juego_monedas(monedas)

    solucion, ganancia_mateo = reconstruir_solucion(memoria, monedas)
    print(f"Ganancia Sophia: {resultado}")
    print(f"Ganancia Mateo: {ganancia_mateo}")
    print("\nMovimientos:\n")
    for elemento in solucion:
        print(elemento)

if __name__ == "__main__":
    path = sys.argv[1]
    main(path)