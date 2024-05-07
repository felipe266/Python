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
    def __init__(self):
         self.data_abertura = datetime.date.today()
         self.transacao = []
    
    def imprimir(self):
        print(f'data de abertura {self.data_abertura}')
        print(f'transações: ')
        for h in self.transacao:
            print('-',h)
        

class Conta:
    def __init__(self,numero, cliente, saldo, limite) -> None:
        self.numero = numero
        self.titular = cliente
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico()
    
    def depositar(self):
        valor = erro_num('Digite uma valor para depositar: ')
        self.saldo += valor
        self.historico.transacao.append(f'Deposito de {valor}')

    def sacar(self):
        while True:
            valor = erro_num('Digite um valor para sacar: ')
            if valor > self.saldo:
                print(f'\033[0;31mO valor de {valor} excedi o seu saldo {self.saldo}\033[m')
            else:
                self.saldo -= valor
                self.historico.transacao.append(f'Saque de {valor}')
                break
    
    def transferir_para(self,destino,remetente):
        while True:
            valor = erro_num('Digite uma valor para transferir: ')
            if valor > self.saldo:
                print(f'\033[0;31mO valor de {valor} excedi o seu saldo {self.saldo}\033[m')
            else:
                remetente.saldo -= valor
                destino.saldo += valor
                if destino:
                    destino.historico.transacao.append(f'Transferencia de {valor} por {remetente.titular.nome} {remetente.titular.sobrenome}')
                    pass
                self.historico.transacao.append(f'Transferencia de {valor} para {destino.titular.nome} {destino.titular.sobrenome}')
                break
    
    def extrato(self):
        print(f'nome: {self.titular.nome} {self.titular.sobrenome} \nCpf: {self.titular.cpf} \nSaldo: {self.saldo}')


cliente1 = Cliente('Felipe','Rodrigues', '111-111-111-11')
cliente2 = Cliente('ana','julia', '222-222-222-22')
c1 = Conta('123-4', cliente1, 1000, 2000)
c2 = Conta('567-8', cliente2, 1500, 2000)
c1.sacar()
c1.depositar()
c1.transferir_para(c2,c1)
print('-='*15)
c1.extrato()
c1.historico.imprimir()
print('-='*15)
c2.extrato()
c2.historico.imprimir()