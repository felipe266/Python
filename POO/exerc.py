import datetime

def erro_num(msg):
    while True:
        try:
            n = float(input(msg).strip().replace(',',('.')))
        except(ValueError, TypeError):
            print(f'\033[0;31mO valor não é válido\033[m')
        else:
            return n


class Cliente:
    def __init__(self,nome='<desconhecido>', sobrenome='<desconhecido>', cpf='000-000-000-00') -> None:
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
 
 
class Historico:
    def __init__(self) -> None:
         self.data_abertura = datetime.date.today()
         self.transacao = []
    
    def historico(self):
        pass
        

class Conta:
    def __init__(self,numero, cliente, saldo, limite) -> None:
        self.numero = numero
        self.titular = cliente
        self.saldo = saldo
        self.limite = limite
    
    def depositar(self):
        valor = erro_num('Digite uma valor para depositar: ')
        self.saldo += valor

    def sacar(self):
        valor = erro_num('Digite um valor para sacar: ')
        self.saldo -= valor
    
    def transferir_para(self,nome,remetente):
        valor = erro_num('Digite uma valor para transferir: ')
        nome.saldo += valor
        remetente.saldo -= valor
    
    def extrato(self):
        print(f'conta 1: \nnome: {self.titular.nome} {self.titular.sobrenome} \nCpf: {self.titular.cpf} \nSaldo: {self.saldo} \ndata de abertura: {self.data_abertura}')


cliente1 = Cliente('Felipe','Rodrigues', '111-111-111-11')
cliente2 = Cliente('ana','julia', '222-222-222-22')
c1 = Conta('123-4', cliente1, 125, 1000)
c2 = Conta('567-8', cliente2, 500, 2000)
c1.extrato()
print('-='*15)
c2.extrato()
print('-='*15)
c1.transferir_para(c2,c1)
print('-='*15)
c1.extrato()
print('-='*15)
c2.extrato()