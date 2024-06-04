#problema do diamante: Se as classes B e C herdarem a classe A e a classe D herdar as classes B e C, e as classes B e C		têm	um método m2(), qual método	a classe D herda?
class A:
    
    def m1(self):
        print('aqui A')


class B(A):
    
    def m1(self):
        super().m1()
    
    def m2(self):
        print('aqui B')


class C(A):
    
    def m1(self):
        super().m1()
    
    def m2(self):
        print('aqui C')


class D(B,C):
    
    def m1(self):
        super().m1()
    
    def m2(self):
        super().m2()

#A ordem de herança da class 1º-B, 2º-C e 3º-A
d = D()
d.m1()
d.m2()

#EXEMPLO
import abc


class Conta:
    
    def __init__(self, numero, nome, saldo):
        self._numero = numero
        self._nome= nome
        self._saldo = saldo
        

class Tributavel(abc.ABC):
    
    @abc.abstractclassmethod
    def valor_imposto(self):
        ...


class ContaCorrente(Conta, Tributavel):
    def __init__(self, numero, nome, saldo):
        super().__init__(numero, nome, saldo)
    
    def valor_imposto(self):
        return self._saldo * 0.01


class Seguro(Tributavel):
    
    def __init__(self, valor, titular, numero_apolice):
        self._valor = valor
        self._titular = titular
        self._numero_apolice = numero_apolice
        
    def valor_imposto(self):
        return 50 + self._valor * 0.05

#class polimorfica
class Manipula_tributos:
    
    def calculo_imposto(self, lista_tributos):
        total = 0
        for t in lista_tributos:
            total += t.valor_imposto()
            
        return total


cc1 = ContaCorrente('123-4','fel', 2500)
cc2 = ContaCorrente('567-8', 'ipe', 3000)

s1 = Seguro(1000,'fel', '357-88')
s2 = Seguro(800, 'ipe', '159-87')

lista_tributos = [cc1, cc2, s1, s2]

manipula = Manipula_tributos()
total = manipula.calculo_imposto(lista_tributos)

print(total)