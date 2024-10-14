from main import *

def _obtener_movimientos(path, delimiter):
    movimientos = []
    with open(path, "r", encoding='utf-8') as f:
        csv_reader = csv.reader(f, delimiter=delimiter)
        for l in csv_reader:
            for mov in l:
                movimientos.append(mov)
    return movimientos

def test_4_monedas():
    monedas = obtener_monedas("./ejemplos/4.txt")
    movimientos_esperados = _obtener_movimientos("./ejemplos/resultados/4_movimientos_esperados.txt", ";")
    acum_sophia, memory = juego_monedas(monedas)
    movimientos, acum_mateo = reconstruir_solucion(memory, monedas)

    assert acum_sophia == 22
    assert acum_mateo == 11
    assert movimientos == movimientos_esperados

def test_5_monedas():
    monedas = obtener_monedas("./ejemplos/5.txt")
    movimientos_esperados = _obtener_movimientos("./ejemplos/resultados/5_movimientos_esperados.txt", ";")
    acum_sophia, memory = juego_monedas(monedas)
    movimientos, acum_mateo = reconstruir_solucion(memory, monedas)

    assert acum_sophia == 1483
    assert acum_mateo == 1268
    assert movimientos == movimientos_esperados

def test_10_monedas():
    monedas = obtener_monedas("./ejemplos/10.txt")
    movimientos_esperados = _obtener_movimientos("./ejemplos/resultados/10_movimientos_esperados.txt", ";")
    acum_sophia, memory = juego_monedas(monedas)
    movimientos, acum_mateo = reconstruir_solucion(memory, monedas)

    assert acum_sophia == 2338
    assert acum_mateo == 1780
    assert movimientos == movimientos_esperados

def test_20_monedas():
    monedas = obtener_monedas("./ejemplos/20.txt")
    movimientos_esperados = _obtener_movimientos("./ejemplos/resultados/20_movimientos_esperados.txt", ";")
    acum_sophia, memory = juego_monedas(monedas)
    movimientos, acum_mateo = reconstruir_solucion(memory, monedas)

    assert acum_sophia == 5234
    assert acum_mateo == 4264
    assert movimientos == movimientos_esperados

def test_25_monedas():
    monedas = obtener_monedas("./ejemplos/25.txt")
    movimientos_esperados = _obtener_movimientos("./ejemplos/resultados/25_movimientos_esperados.txt", ";")
    acum_sophia, memory = juego_monedas(monedas)
    movimientos, acum_mateo = reconstruir_solucion(memory, monedas)

    assert acum_sophia == 7491
    assert acum_mateo == 6523
    assert movimientos == movimientos_esperados

def test_50_monedas():
    monedas = obtener_monedas("./ejemplos/50.txt")
    movimientos_esperados = _obtener_movimientos("./ejemplos/resultados/50_movimientos_esperados.txt", ";")
    acum_sophia, memory = juego_monedas(monedas)
    movimientos, acum_mateo = reconstruir_solucion(memory, monedas)

    assert acum_sophia == 14976
    assert acum_mateo == 13449
    assert movimientos == movimientos_esperados

def test_100_monedas():
    monedas = obtener_monedas("./ejemplos/100.txt")
    movimientos_esperados = _obtener_movimientos("./ejemplos/resultados/100_movimientos_esperados.txt", ";")
    acum_sophia, memory = juego_monedas(monedas)
    movimientos, acum_mateo = reconstruir_solucion(memory, monedas)

    assert acum_sophia == 28844
    assert acum_mateo == 22095
    assert movimientos == movimientos_esperados

def test_1000_monedas():
    monedas = obtener_monedas("./ejemplos/1000.txt")
    movimientos_esperados = _obtener_movimientos("./ejemplos/resultados/1000_movimientos_esperados.txt", ";")
    acum_sophia, memory = juego_monedas(monedas)
    movimientos, acum_mateo = reconstruir_solucion(memory, monedas)

    assert acum_sophia == 1401590
    assert acum_mateo == 1044067
    assert movimientos == movimientos_esperados

def test_2000_monedas():
    monedas = obtener_monedas("./ejemplos/2000.txt")
    movimientos_esperados = _obtener_movimientos("./ejemplos/resultados/2000_movimientos_esperados.txt", ";")
    acum_sophia, memory = juego_monedas(monedas)
    movimientos, acum_mateo = reconstruir_solucion(memory, monedas)

    assert acum_sophia == 2869340
    assert acum_mateo == 2155520
    assert movimientos == movimientos_esperados

def test_5000_monedas():
    monedas = obtener_monedas("./ejemplos/5000.txt")
    movimientos_esperados = _obtener_movimientos("./ejemplos/resultados/5000_movimientos_esperados.txt", ";")
    acum_sophia, memory = juego_monedas(monedas)
    movimientos, acum_mateo = reconstruir_solucion(memory, monedas)

    assert acum_sophia == 9939221
    assert acum_mateo == 7617856
    assert movimientos == movimientos_esperados

# Nota: Comentar este test si se quiere ejecutar las pruebas rapidamente
def test_10000_monedas():
    monedas = obtener_monedas("./ejemplos/10000.txt")
    movimientos_esperados = _obtener_movimientos("./ejemplos/resultados/10000_movimientos_esperados.txt", ";")
    acum_sophia, memory = juego_monedas(monedas)
    movimientos, acum_mateo = reconstruir_solucion(memory, monedas)

    assert acum_sophia == 34107537
    assert acum_mateo == 25730392
    assert movimientos == movimientos_esperados
