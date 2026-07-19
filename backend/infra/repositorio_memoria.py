from typing import Optional
from domain.modelo import ModeloLpco


class RepositorioMemoria:
    def __init__(self):
        self._modelos = [
            ModeloLpco(1, "LPCO-0001", "MAPA", "Produtos de origem vegetal", 24),
            ModeloLpco(2, "LPCO-0002", "ANVISA", "Produtos para saúde", 31),
            ModeloLpco(3, "LPCO-0003", "IBAMA", "Produtos florestais", 18),
        ]

    def listar(self) -> list[ModeloLpco]:
        return list(self._modelos)

    def obter_por_id(self, modelo_id: int) -> Optional[ModeloLpco]:
        return next((m for m in self._modelos if m.id == modelo_id), None)