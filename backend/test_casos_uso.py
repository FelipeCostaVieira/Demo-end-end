from aplication.casos_uso import ObterModelo, ModeloNaoEncontrado
from domain.modelo import ModeloLpco
import pytest


class RepositorioFake:
    def listar(self):
        return [ModeloLpco(1, "LPCO-0001", "MAPA", "Teste", 10)]

    def obter_por_id(self, modelo_id):
        return self.listar()[0] if modelo_id == 1 else None


def test_obter_modelo_inexistente_levanta_excecao():
    caso_uso = ObterModelo(RepositorioFake())
    with pytest.raises(ModeloNaoEncontrado):
        caso_uso.executar(999)