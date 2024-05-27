class Conta:
    
    def __init__(self, numero, titular, saldo, contas = 0, limite = 1000):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self.limite = limite
        self.contas = contas
        contas += 1
    
    #como as funçoes sao "privadas" as def fazem o encapsulamento dos self para para fazer operações dentro da própria class
    def pega_saldo(self):
        print(f'seu saldo é de {self._saldo}')
    
    def depositar(self, saldo):
        self._saldo += saldo
    
    def retirar(self, saldo):
        self._saldo -= saldo
    
    #property funciona como um getter nas linguagens, java e C#.Funciona para recuperar dados, ou seja retorna dados
    @property
    def saldo(self):
        return (f'seu saldo {self._saldo}')
    
    #aqui funciona como um modificador de dadsos
    @saldo.setter
    def saldo(self, saldo):
        if saldo < 0:
            print('saldo não pode ser negativo')
        else:
            self._saldo = saldo
    #atulização disso é bem especifica, como desse caso não necessariamente precisamps do property pois podiamos manipular usando as def, manipulando e retirar
    
    
    
c = Conta('123-4', 'felipe', 1000)
c.saldo = -300
print(c.contas)