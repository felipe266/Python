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

class Conta:
    def __init__(self,saldo=0.0):
        self._saldo = saldo
    
    @property
    def saldo(self) -> int:
        return self._saldo
    
    @saldo.setter
    def saldo(self, saldo):
        if saldo < 0:
            print('\033[0;31mSaldo não pode ser negativo\033[m')
        else:
            self._saldo = saldo

c = Conta(10000)
c.saldo = -300