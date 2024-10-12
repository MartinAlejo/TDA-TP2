from main import *

# De momento no se usa (una vez que tengamos la reconstruccion del camino, si)
# def _obtener_movimientos(path, delimiter):
#     movimientos = []
#     with open(path, "r", encoding='utf-8') as f:
#         csv_reader = csv.reader(f, delimiter=delimiter)
#         for l in csv_reader:
#             for mov in l:
#                 movimientos.append(mov)
#     return movimientos

def test_4_monedas():
    monedas = obtener_monedas("./ejemplos/4.txt")
    #movimientos_esperados = _obtener_movimientos("./ejemplos/5_movimientos_esperados.txt")
    #movimientos, acum_sophia, acum_mateo = juego_monedas(monedas)
    acum_sophia = juego_monedas(monedas)

    assert acum_sophia == 22

def test_5_monedas():
    monedas = obtener_monedas("./ejemplos/5.txt")
    #movimientos_esperados = _obtener_movimientos("./ejemplos/5_movimientos_esperados.txt")
    #movimientos, acum_sophia, acum_mateo = juego_monedas(monedas)
    acum_sophia = juego_monedas(monedas)

    assert acum_sophia == 1483

def test_10_monedas():
    monedas = obtener_monedas("./ejemplos/10.txt")
    acum_sophia = juego_monedas(monedas)

    assert acum_sophia == 2338

def test_20_monedas():
    monedas = obtener_monedas("./ejemplos/20.txt")
    acum_sophia = juego_monedas(monedas)

    assert acum_sophia == 5234

def test_25_monedas():
    monedas = obtener_monedas("./ejemplos/25.txt")
    acum_sophia = juego_monedas(monedas)

    assert acum_sophia == 7491

def test_50_monedas():
    monedas = obtener_monedas("./ejemplos/50.txt")
    acum_sophia = juego_monedas(monedas)

    assert acum_sophia == 14976

# TODO: FALLA (quiza error de la catedra)
def test_100_monedas():
    monedas = obtener_monedas("./ejemplos/100.txt")
    acum_sophia = juego_monedas(monedas)

    assert acum_sophia == 28844

def test_1000_monedas():
    monedas = obtener_monedas("./ejemplos/1000.txt")
    acum_sophia = juego_monedas(monedas)

    assert acum_sophia == 1401590

def test_2000_monedas():
    monedas = obtener_monedas("./ejemplos/2000.txt")
    acum_sophia = juego_monedas(monedas)

    assert acum_sophia == 2869340

def test_5000_monedas():
    monedas = obtener_monedas("./ejemplos/5000.txt")
    acum_sophia = juego_monedas(monedas)

    assert acum_sophia == 9939221

# Nota: Comentar este test si se quiere ejecutar las pruebas rapidamente
def test_10000_monedas():
    monedas = obtener_monedas("./ejemplos/10000.txt")
    acum_sophia = juego_monedas(monedas)

    assert acum_sophia == 34107537
