from pydantic import BaseModel


class ModeloResposta(BaseModel):
    id: int
    codigo: str
    orgao: str
    descricao: str
    campos: int