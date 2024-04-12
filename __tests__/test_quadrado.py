# bibliotecas
import pytest

# funcoes
from quadrado.quadrado import calcular_area_quadrado, calcular_area_retangulo, calcular_area_triangulo
from utils.utils import ler_csv 

# testes
def test_calcular_area_quadrado():
    lado1 = 5
    resultado_esperado = 25
    resultado_obtido = calcular_area_quadrado(lado1)
    assert resultado_esperado == resultado_obtido

def test_calcular_area_retangulo():
    comp1 = 6
    larg1 = 5
    resultado_esperado = 30
    resultado_obtido = calcular_area_retangulo(comp1, larg1)
    assert resultado_esperado == resultado_obtido

def test_calcular_area_triangulo():
    bas1 = 20
    alt1 = 20
    resultado_esperado = 200
    resultado_obtido = calcular_area_triangulo(bas1, alt1)
    assert resultado_esperado == resultado_obtido

@pytest.mark.parametrize('bas1, alt1, resultado_esperado',
                         [
                             (10,5,25),
                             (2,4,4),
                             (5,15,37.5),
                             (110,2,110)
                         ]
                         )

def test_calcular_area_triangulo_lista(bas1,alt1,resultado_esperado):
    resultado_obtido = calcular_area_triangulo (bas1,alt1)
    assert resultado_esperado == resultado_obtido

@pytest.mark.parametrize('bas1,alt1,resultado_esperado',
                         ler_csv('./fixtures/massa_area.csv')
                         )

def test_calcular_area_triangulo_lista(bas1,alt1,resultado_esperado):
    resultado_obtido = calcular_area_triangulo(float (bas1), float (alt1))
    assert float (resultado_esperado) == resultado_obtido