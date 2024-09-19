import numpy as np
import pytest

from meu_modulo.vetor import VetorReal


@pytest.fixture
def valores_de_vetor():
    tamanho_aleatorio = np.random.randint(1, 10)
    aleatorios = np.random.rand(tamanho_aleatorio)
    return aleatorios
