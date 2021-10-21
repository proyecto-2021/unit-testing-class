from maximo import maximo, m


def test_maximo_primero_menor_que_segundo():
    # Elegir entradas para tester el SUT
    a = 2
    b = 3
    # Ejecutar el SUT para dichas entradas
    res = maximo(a, b)
    # Verificar el comportamiento esperado del SUT
    assert res == 3



def test_maximo_segundo_menor_que_primero():
    # Elegir entradas para tester el SUT
    a = 5
    b = 2
    # Ejecutar el SUT para dichas entradas
    res = maximo(a, b)
    # Verificar el comportamiento esperado del SUT
    assert res == 5



def test_m():
    res = m(10, 5)
    assert res == 10

def test_bug_m():
    res = m(5, 10)
    assert res == 10