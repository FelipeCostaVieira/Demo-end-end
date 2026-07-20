# Demo LPCO — API + Front

Fatia full-stack demonstrando consulta de modelos LPCO (Licença, Permissão, 
Certificado), usados no licenciamento de importação do Portal Único Siscomex.

O objetivo é exercitar, de ponta a ponta, uma arquitetura de API em Python 
desacoplada de um front em TypeScript, sobre um domínio real de comércio 
exterior.

## Stack

- **Back-end:** Python + FastAPI (documentação automática em `/docs`), 
  validação com Pydantic
- **Front-end:** React + TypeScript + Vite + TanStack Query
- **Testes:** pytest

## Como rodar

**API** (porta 8000):

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # Linux/macOS
pip install fastapi "uvicorn[standard]"
uvicorn main:app --reload
```

Documentação interativa em `http://127.0.0.1:8000/docs`.

**Front** (porta 5173):

```bash
cd frontend
npm install
npm run dev
```

**Testes:**

```bash
cd backend
pip install pytest httpx
pytest -v
```

## Decisões técnicas

- **TanStack Query** em vez de `useState` + `useEffect`: dado remoto é cache 
  com ciclo de vida, não estado local. A biblioteca cuida de deduplicação, 
  retry e revalidação, resolvendo em outra camada o mesmo problema de 
  resiliência que trato manualmente em integrações do Siscomex.
- **Pydantic no contrato de saída** (`response_model`): valida a resposta, 
  documenta o schema no `/docs` e evita vazar campos não declarados.
- **Tratamento de erro correto:** recurso inexistente retorna 404 via 
  `HTTPException`, não 200 com corpo de erro. Este comportamento foi 
  descoberto por um teste que documentava a versão incorreta.
- **CORS restrito** à origem do front em desenvolvimento, em vez de liberar 
  geral.
- **Domínio LPCO:** modelagem baseada em experiência real com integrações 
  do Portal Único Siscomex.

## Testes

Os testes de integração exercitam a API pela borda (HTTP), cobrindo contrato 
de status, forma do dado e os caminhos feliz e de erro (recurso existente e 
inexistente).

## Arquitetura em camadas

O `main` mantém o demo intencionalmente simples. A branch 
[`arquitetura-camadas`](../../tree/arquitetura-camadas) contém um refactor 
para camadas (domínio, aplicação, infraestrutura, API), demonstrando 
inversão de dependência e testes de unidade isolados do framework. Para um 
demo desta dimensão, camadas são mais do que o necessário; o objetivo é 
exercitar o padrão e documentar como o projeto evoluiria.