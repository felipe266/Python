'''class Conta:
    
    def __init__(self, nome, cpf, saldo):
        self._nome = nome
        self._cpf = cpf
        self._saldo = saldo
    
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa
        return self._saldo
    
    def __str__(self) -> str:
        return f'dados da conta: \nNome: {self._nome} \nCpf: {self._cpf} \nSaldo: {self._saldo}'
    

class ContaCorrent(Conta):
    
    def __init__(self, nome, cpf, saldo):
        super().__init__(nome, cpf, saldo)
    
    def atualiza(self, taxa):
        self._saldo += self._saldo *(2*taxa)
        return self._saldo
    
    def depositar(self, valor):
        self._saldo += valor - 0.1


class ContaPoupanca(Conta):
    
    def __init__(self, nome, cpf, saldo):
        super().__init__(nome, cpf, saldo)
    
    def atualiza(self, taxa):
        self._saldo += self._saldo *(3*taxa)
        return self._saldo
    


class AtualizaContas:
    
    def __init__(self, selic, saldo_total=0):
        self._selic = selic
        self._saldo_total = saldo_total
    
    def roda(self,conta):
        print(f'Saldo da Conta: {conta._saldo:.2f}')
        self._saldo_total += conta.atualiza(self._selic)
        print(f'Saldo final: {self._saldo_total:.2f}')
        print('=-'*15)
        
        
c = Conta('felipe', '111.111.111-11', 1500)
cc = ContaCorrent('jose', '222.222.222-22', 2000)
cp = ContaPoupanca('maria', '333.333.333-330', 2500)
at = AtualizaContas(0.105)

c.atualiza(0.02)
cc.atualiza(0.02)
cp.atualiza(0.02)

at.roda(c)
at.roda(cc)
at.roda(cp)

print(c)
print(cc)
print(cp)'''

#exercício opcional
class Banco:
    
    def __init__(self):
        self._contas = []
    
    def adiciona(self, conta):
        self._contas.append({'Nome': conta._nome, 'Cpf': conta._cpf, 'Saldo': conta._saldo, 'tipo': conta._tipo})

    def pega_conta(self, pos):
        return self._contas[pos]
    
    def tot_contas(self):
        return len(self._contas)


class Conta1:
    
    _total_contas = 0
    
    def __init__(self, nome, cpf, saldo, tipo):
        self._nome = nome
        self._cpf = cpf
        self._saldo = saldo
        self._tipo = tipo
        self._banco = Banco()
        self._banco.adiciona()
        self._identificador = Conta1._total_contas
        Conta1._total_contas += 1
    
    
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa
        Banco()._contas[self._identificador]['saldo'] = self._saldo
        return self._saldo
    
    def __str__(self):
        return f'Nome: {self._nome} \nCpf: {self._cpf} \nSaldo: {self._saldo} \nposição: {self._identificador} \nTipo: {self._tipo}'
    

class AtualizaContas:
    
    def __init__(self, selic, saldo_total=0):
        self._selic = selic
        self._saldo_total = saldo_total
    
    def roda(self,conta):
        print(f'Saldo da Conta: {conta._saldo:.2f}')
        self._saldo_total += conta.atualiza(self._selic)
        print(f'Saldo final: {self._saldo_total:.2f}')
        print('=-'*15)
    

c = Conta1('felipe','111.111.111-11', 1500, 'corrente')
c2 = Conta1('rival','222.222.222-22', 2500, 'popança')

at = AtualizaContas(0.105)

at.roda(c2)

print(b._contas)