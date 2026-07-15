from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Demo Comex API")

# Permite que o front (Vite, porta 5173) consuma esta API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

MODELOS_LPCO = [
    {"id": 1, "codigo": "LPCO-0001", "orgao": "MAPA", "descricao": "Produtos de origem vegetal", "campos": 24},
    {"id": 2, "codigo": "LPCO-0002", "orgao": "ANVISA", "descricao": "Produtos para saúde", "campos": 31},
    {"id": 3, "codigo": "LPCO-0003", "orgao": "IBAMA", "descricao": "Produtos florestais", "campos": 18},
    {"id": 4, "codigo": "LPCO-0004", "orgao": "DECEX", "descricao": "Licenciamento automático", "campos": 12},
    {"id": 5, "codigo": "LPCO-0005", "orgao": "ANP", "descricao": "Combustíveis e derivados", "campos": 27},
]


@app.get("/modelos")
def listar_modelos():
    return MODELOS_LPCO


@app.get("/modelos/{modelo_id}")
def obter_modelo(modelo_id: int):
    for modelo in MODELOS_LPCO:
        if modelo["id"] == modelo_id:
            return modelo
    return {"erro": "Modelo não encontrado"}