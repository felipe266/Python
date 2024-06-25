from dataclasses import dataclass
from categoria import Categoria


@dataclass
class Transacao:
    descricao: str
    valor: int
    categoria: Categoria