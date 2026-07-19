from typing import Protocol, Optional
from domain.modelo import ModeloLpco


class RepositorioModelos(Protocol):
    def listar(self) -> list[ModeloLpco]: ...
    def obter_por_id(self, modelo_id: int) -> Optional[ModeloLpco]: ...