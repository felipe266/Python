from dataclasses import dataclass
from categoria import Categoria


@dataclass
class Transacao:
    descricao: str
    valor: int
    categoria: Categoria
    
    def exibir(self):
        print(f'Descrição: {self.descricao} \nValor: {self.valor} \nCategoria: {self.categoria.nome}')
