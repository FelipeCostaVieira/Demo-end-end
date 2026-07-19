from dataclasses import dataclass


@dataclass(frozen=True)
class ModeloLpco:
    id: int
    codigo: str
    orgao: str
    descricao: str
    campos: int

    def exige_atributos_ncm(self) -> bool:
        """Regra de negócio: alguns órgãos exigem atributos de NCM."""
        return self.orgao in {"ANVISA", "MAPA"}