from fastapi import FastAPI
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Demo Comex API")

# Permite que o front (Vite, porta 5173) consuma esta API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Endpoints da API 
class Modelo(BaseModel):
    id: int
    codigo: str
    orgao: str
    descricao: str
    campos: int


# Dados simulados para os modelos de LPCO
MODELOS_LPCO = [
    {"id": 1, "codigo": "LPCO-0001", "orgao": "MAPA", "descricao": "Produtos de origem vegetal", "campos": 24},
    {"id": 2, "codigo": "LPCO-0002", "orgao": "ANVISA", "descricao": "Produtos para saúde", "campos": 31},
    {"id": 3, "codigo": "LPCO-0003", "orgao": "IBAMA", "descricao": "Produtos florestais", "campos": 18},
    {"id": 4, "codigo": "LPCO-0004", "orgao": "DECEX", "descricao": "Licenciamento automático", "campos": 12},
    {"id": 5, "codigo": "LPCO-0005", "orgao": "ANP", "descricao": "Combustíveis e derivados", "campos": 27},
]



@app.get("/modelos", response_model=list[Modelo])
def listar_modelos():
    return MODELOS_LPCO

@app.get("/modelos/{modelo_id}")
def obter_modelo(modelo_id: int):
    for modelo in MODELOS_LPCO:
        if modelo["id"] == modelo_id:
            return modelo
    raise HTTPException(status_code=404, detail="Modelo não encontrado")

