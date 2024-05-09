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
    
    __slots__ = ['_numero', '_titular', '_saldo', '_limite','historico','_identificador']
    _total_contas = 1
    
    def __init__(self,numero, cliente, saldo, limite):
        self._numero = numero
        self._titular = cliente
        self._saldo = saldo
        self._limite = limite
        self.historico = Historico()
        self._identificador = Conta._total_contas
        Conta._total_contas += 1
        #ao colocar o '__' deixa o atributo "privado", assim esses atributos não poderam ser mechidos fora da class,porém apenas '_' já é entre programadores
    
    def depositar(self):
        valor = erro_num('Digite uma valor para depositar: ')
        self._saldo += valor
        self.historico.transacao.append(f'Deposito de {valor}')

    def sacar(self):
        while True:
            valor = erro_num('Digite um valor para sacar: ')
            if valor > self._saldo:
                print(f'\033[0;31mO valor de {valor} excedi o seu saldo {self.saldo}\033[m')
            else:
                self._saldo -= valor
                self.historico.transacao.append(f'Saque de {valor}')
                break
    
    def transferir_para(self,destino,remetente):
        while True:
            valor = erro_num('Digite uma valor para transferir: ')
            if valor > self._saldo:
                print(f'\033[0;31mO valor de {valor} excedi o seu saldo {self._saldo}\033[m')
            else:
                remetente._saldo -= valor
                destino._saldo += valor
                if destino:
                    destino.historico.transacao.append(f'Transferencia de {valor} por {remetente._titular.nome} {remetente._titular.sobrenome}')
                self.historico.transacao.append(f'Transferencia de {valor} para {destino._titular.nome} {destino._titular.sobrenome}')
                break
    
    def extrato(self):
        print(f'informações da conta {self._identificador} \nSaldo: {self._saldo}')


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