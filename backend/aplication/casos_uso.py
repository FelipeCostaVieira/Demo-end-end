from domain.modelo import ModeloLpco
from domain.repositorio import RepositorioModelos


class ModeloNaoEncontrado(Exception):
    pass


class ListarModelos:
    def __init__(self, repositorio: RepositorioModelos):
        self._repositorio = repositorio

    def executar(self) -> list[ModeloLpco]:
        return self._repositorio.listar()


class ObterModelo:
    def __init__(self, repositorio: RepositorioModelos):
        self._repositorio = repositorio

    def executar(self, modelo_id: int) -> ModeloLpco:
        modelo = self._repositorio.obter_por_id(modelo_id)
        if modelo is None:
            raise ModeloNaoEncontrado(f"Modelo {modelo_id} não existe")
        return modelo