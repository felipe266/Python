#1-inicializador
class Conta:
    
    #os slostes serem para que o usuario não crie novos atributos fora da class, e servem para economizar memória, serca de 40 a 55%
    __slots__ = ['_saldo', '_titular', '_identificador']
    
    _total_contas = 0
    
    def __init__(self, saldo, titular):
        self._saldo = saldo
        self._titular = titular
        Conta._total_contas += 1
        self._identificador = Conta._total_contas
    
    #esse métado permite que a def seje estático, ou seja não precisa de um variavel para receber
    @staticmethod
    def contas():
        return f'total de contas é {Conta._total_contas}'
    
    #temos também o metado de classe. Servem para definor um métado que opera  na class
    @classmethod
    def tcontas(cls):
        return f'total de contas é {cls._total_contas}' 

c = Conta(1000, 'felipe')

#deu erro 
'''c.nome = 'felie'''

print(c.tcontas())

c2 = Conta(1040, 'nar')

print(c2.tcontas())