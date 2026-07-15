import { useQuery } from '@tanstack/react-query'

type Modelo = {
  id: number
  codigo: string
  orgao: string
  descricao: string
  campos: number
}

async function buscarModelos(): Promise<Modelo[]> {
  const resposta = await fetch('http://127.0.0.1:8000/modelos')
  if (!resposta.ok) {
    throw new Error(`Falha ao buscar modelos: ${resposta.status}`)
  }
  return resposta.json()
}

export default function App() {
  const { data, isPending, isError, error, refetch, isFetching } = useQuery({
    queryKey: ['modelos'],
    queryFn: buscarModelos,
  })

  if (isPending) return <p style={{ padding: 24 }}>Carregando modelos...</p>

  if (isError)
    return (
      <div style={{ padding: 24 }}>
        <p style={{ color: 'crimson' }}>Erro: {error.message}</p>
        <button onClick={() => refetch()}>Tentar novamente</button>
      </div>
    )

  return (
    <div style={{ padding: 24, fontFamily: 'system-ui' }}>
      <h1>Modelos LPCO</h1>
      <button onClick={() => refetch()} disabled={isFetching}>
        {isFetching ? 'Atualizando...' : 'Atualizar'}
      </button>

      <table style={{ marginTop: 16, borderCollapse: 'collapse' }}>
        <thead>
          <tr>
            <th style={{ textAlign: 'left', padding: 8 }}>Código</th>
            <th style={{ textAlign: 'left', padding: 8 }}>Órgão</th>
            <th style={{ textAlign: 'left', padding: 8 }}>Descrição</th>
            <th style={{ textAlign: 'left', padding: 8 }}>Campos</th>
          </tr>
        </thead>
        <tbody>
          {data.map((m) => (
            <tr key={m.id} style={{ borderTop: '1px solid #ddd' }}>
              <td style={{ padding: 8 }}>{m.codigo}</td>
              <td style={{ padding: 8 }}>{m.orgao}</td>
              <td style={{ padding: 8 }}>{m.descricao}</td>
              <td style={{ padding: 8 }}>{m.campos}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}