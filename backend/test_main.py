from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_listar_modelos_retorna_200():
    resposta = client.get("/modelos")
    assert resposta.status_code == 200


def test_listar_modelos_retorna_lista_nao_vazia():
    dados = client.get("/modelos").json()
    assert isinstance(dados, list)
    assert len(dados) > 0


def test_modelo_tem_campos_obrigatorios():
    modelo = client.get("/modelos").json()[0]
    for campo in ("id", "codigo", "orgao", "descricao", "campos"):
        assert campo in modelo


def test_obter_modelo_existente():
    resposta = client.get("/modelos/1")
    assert resposta.status_code == 200
    assert resposta.json()["codigo"] == "LPCO-0001"


def test_obter_modelo_inexistente():
    resposta = client.get("/modelos/999")
    assert "erro" in resposta.json()