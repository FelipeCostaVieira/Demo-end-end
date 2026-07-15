# Demo LPCO — API + Front

Fatia full-stack demonstrando consulta de modelos LPCO (Licença, Permissão, Certificado),
usados no licenciamento de importação do Portal Único Siscomex.

## Stack
- **Back-end:** Python 3 + FastAPI (documentação automática em `/docs`)
- **Front-end:** React + TypeScript + Vite + TanStack Query

## Como rodar

**API** (porta 8000):
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install fastapi "uvicorn[standard]"
uvicorn main:app --reload

**Front** (porta 5173):
cd frontend
npm install
npm run dev

## Decisões técnicas
- **TanStack Query** em vez de `useState` + `useEffect`: dado remoto é cache com ciclo de
  vida, não estado local. A biblioteca cuida de deduplicação, retry e revalidação.
- **CORS restrito** à origem do front em desenvolvimento, em vez de liberar geral.
- **Domínio LPCO**: modelagem baseada em experiência real com integrações do Siscomex.
