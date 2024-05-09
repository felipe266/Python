class Pessoas:
    def __init__(self,idade):
        self.__idade = idade  
    
pessoa = Pessoas(20)
print(pessoa._Pessoas__idade)
#encapsulamento parecido com java----------
class Conta1:
    def __init__(self,saldo):
        self._saldo = saldo
    
    def get_saldo(self) -> int:
        return self._saldo

    def set_saldo(self, saldo):
        self._saldo = saldo

c1 = Conta1(150)
c2 = Conta1(300)
c3 = Conta1(-200)
print(c1.get_saldo())

print(c2.get_saldo())

c3.set_saldo(c1.get_saldo() + c2.get_saldo())
print(c3.get_saldo())
#forma pythônica--------------

class Conta():
    
    _total_contas = 0
    
    #__slots__ apagam a __dict__ da variavel recebendo Conta e também nao deixa criar novos atributos.
    __slots__ = ['_numero', '_titular', '_saldo', '_limite']
    
    def __init__(self, saldo, numero=0, titular=0, limite=1000):
        self._saldo = saldo
        self._numero = numero
        self._titular = titular
        self._limite = limite
        Conta._total_contas += 1
    
    @property
    def saudo(self) -> int:
        return self._saldo
    
    @saudo.setter
    def saudo(self, saldo):
        if saldo < 0:
            print('\033[0;31mSaldo não pode ser negativo\033[m')
        else:
            self._saldo = saldo
    #métado estático(é usado quando não deseja receber nem um parâmetro e só envia vairaveis inicializados ou return)---------------
    '''@staticmethod
    def tota_contas() -> str:
        return Conta._total_contas'''
    
    #métado de classes(servem para definir um métado que opera na class e não na instancia)-------------
    @classmethod
    def tota_contas(cls):
        return cls._total_contas


c = Conta(10000)
c.saudo = -300
print(c.tota_contas())
c2 = Conta(1500)
print(c.tota_contas())
#classmethod e staticmethod são as mesmas bem parecidos so que o 1 é dentro da class e o outro é fora
print(Conta.tota_contas())