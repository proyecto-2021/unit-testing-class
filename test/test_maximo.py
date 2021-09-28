from maximo import maximo


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
