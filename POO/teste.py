class teste():
    def fib(n):
        if n == 0 or n == 1:
            return n
        return teste.fib(n-1) + teste.fib(n-2)
    

    def dic(**vari):
        for k, v in vari.items():
            print(f'{k}: {v}')


    def par_impa(i, f):
        if i < f:
            for n in range(i,f+1):
                if n%2 == 0:
                    print(f'O {n} é par')
                    continue
                print(f'o {n} é impar')
        if i > f:
            for n in range(f,i+1):
                if n%2 == 0:
                    print(f'O {n} é par')
                    continue
                print(f'o {n} é impar')
    
    
    def soma(n = 0, b = 0) -> int:
        return n + b
    def seila(ola):
        pass
 

print(teste.soma.__annotations__)
#o '->' declara o tipo do retorno da função
#pass funciona como 'vou penssar
print(teste.fib(6))
print('~~'*10)
vari = teste.dic(nome = 'felipe', idade = 21, email = 'felipe@felipe')
print('~~'*15)
vari = teste.dic(**{'nome':'felipe', 'idade': 21, 'email':'felipe@felipe'})
print('~~'*15)
teste.par_impa(10,5)
print('~~'*15)
#--------------------------------------------------------------------------
#OBS: dentro de uma class só renotornam valores dentro de uma def
#--------------------------------------------------------------------------
import datetime

class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf


class Historico:
    def __init__(self):
        self.data_abertura = datetime.date.today()
        self.transacoes = []

    def imprime(self):
        print(f'data de abertura {self.data_abertura}')
        print('transações: ')
        for t in self.transacoes:
            print('-',t)


class Conta:
    def __init__(self,numero, cliente, saldo, limite):
        self.numero = numero
        self.titular = cliente
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico()

    def erro(self, msg):
        while True:    
            try:
                valor = float(input(msg))
            except (TypeError, ValueError):
                print('Algo de errado não deu certo')
            else:
                return valor
            
    def depositar(self,msg='', v =0):
        if msg not in '':
            valor = self.erro(msg)
        else:
            valor = v
            self.saldo += valor
        self.saldo += valor
        self.historico.transacoes.append(f'deposito de {valor}')

    def sacar(self, msg='', v = 0):
        if msg not in '':
            valor = self.erro(msg)
            self.saldo -= valor
        else:
            valor = v
            self.saldo -= valor
        self.historico.transacoes.append(f'sacamento de {valor}')
    
    def extrato(self):
        print(f'número: {self.numero} \nsaldo: {self.saldo}')
    
    def transfere_para(self, msg, destino):
        retirou = self.erro(msg)
        while True:
            if retirou > self.saldo:
                print(f'seu saldo é {self.saldo} e não pode ser transferido')
                retirou = self.erro(msg)
            else:
                self.sacar(v = retirou)
                destino.depositar(v=retirou)
                self.historico.transacoes.append(f'transação de {retirou}')
                return retirou

#interlaçando classes-------------
cliente1 = Cliente('Felipe','Rodrigues', '111111-11')
#Uma variarel self recebendo uma class---------------
conta1 = Conta('123-4', cliente1, 1200, 2000)
cliente2 = Cliente('Rivaldo','Felix', '2222222-22')
conta2 = Conta('567-8', cliente2, 1300, 2500)
#brincando com os def-----------------------
conta1.depositar(msg='valor a depositar: ')
conta1.extrato()
print('-='*15)
conta1.sacar(msg='Valor a sacar: ')
conta1.extrato()
print('-='*15)
trans = conta1.transfere_para(msg='Valor a transferir: ', destino= conta2)
conta1.extrato()
#interlaçando classes-------------
print('-='*15)
print(conta1.titular.nome)
print('-='*15)
conta1.historico.imprime()
print('-='*15)
conta2.historico.imprime()
print('-='*15)
print(vars(conta1))