from fastapi import APIRouter, Depends, HTTPException
from aplication.casos_uso import ListarModelos, ObterModelo, ModeloNaoEncontrado
from infra.repositorio_memoria import RepositorioMemoria
from api.schemas import ModeloResposta

router = APIRouter()
_repositorio = RepositorioMemoria()


def obter_listar_modelos() -> ListarModelos:
    return ListarModelos(_repositorio)


def obter_obter_modelo() -> ObterModelo:
    return ObterModelo(_repositorio)


@router.get("/modelos", response_model=list[ModeloResposta])
def listar(caso_uso: ListarModelos = Depends(obter_listar_modelos)):
    return caso_uso.executar()


@router.get("/modelos/{modelo_id}", response_model=ModeloResposta)
def obter(modelo_id: int, caso_uso: ObterModelo = Depends(obter_obter_modelo)):
    try:
        return caso_uso.executar(modelo_id)
    except ModeloNaoEncontrado:
        raise HTTPException(status_code=404, detail="Modelo não encontrado")