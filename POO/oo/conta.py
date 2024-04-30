class Conta:
    def __init__(self, numero,titular,saldo,limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
    
    def depositar(self, valor):
        self.saldo += valor
    
    def sacar(self, valor):
        if self.saldo > valor:
            self.saldo -= valor
            return True
        else:
            return False

    def transfere_para(self, destino, valor):
        pass
    
    def extrato(self):
        print(f'número: {self.numero} \nsaldo: {self.saldo}')