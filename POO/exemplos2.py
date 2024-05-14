import abc

class Funcionario(abc.ABC):
    
    def __init__(self, nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario
    
    #ao colocarmos isso, todas as classes que herdarem de funcionario(filhas) será obrigatório da def bonificacao
    @abc.abstractclassmethod
    def bonificacao(self):
        return self._salario * 0.1


#isso é uma herança, colocamos super() para dizer que, Gerente é uma sublasse de Funcionário 
class Gerente(Funcionario):
    
    def __init__(self,nome, cpf, salario, senha, qtd_funcionario):
        super().__init__(nome, cpf, salario)
        self._senha = senha
        self.qtd_funcionario = qtd_funcionario
    

    def autentica(self, senha):
        if self._senha == senha:
            print('\033[0;32macesso permitido\033[m')
        else:
            print('\033[0;31macesso negado\033[m')
    
    def bonificacao(self):
        return self._salario * 0.15

class Cliente():
    def __init__(self, nome, cpf, saldo):
        self._nome = nome
        self._cpf = cpf
        self._saldo = saldo

class control_bonificacao:
    
    def __init__(self, total_bonificacao=0):
        self._total_bonificacao = total_bonificacao
    
    def registra(self, funcionario):
        try:
            self._total_bonificacao += funcionario.bonificacao()
        except AttributeError as e:
            print(e)
    
    @property
    def total_bonificacao(self):
        return self._total_bonificacao


g = Gerente('felipe', '111.111.111-11', 5000, '123', 0)
print(f'bonificacao gerente: {g.bonificacao()}')

f = Funcionario('rivae','222.222.222-22', 4000)
print(f'bonificacao funcionario: {f.bonificacao()}')

c = Cliente('julia', '333.333.333-33', 1500)

controle = control_bonificacao()
controle.registra(f)
controle.registra(g)
controle.registra(c)

print(f'total: {controle.total_bonificacao}')

print(f.bonificacao())
print(g.bonificacao())
#perceba que cada def bonificação ira pertencer a sua classe, mas bonificação só estiver em funcionario, ela será global
print(vars(g))
print(vars(f))

class Gerente1(Funcionario):
    
    def __str__(self):
        return f'< Instância de {self.__class__.__name__}; endereço: {id(self)}'
    
    def __init__(self, senha, salario):
        self._senha = senha
        self._salario = salario
    
    def bonificacao(self):
        return super().bonificacao() + 1000

g = Gerente1('123', 5000)
print(g.bonificacao())
print(g)
x = 1
print(eval('x + 1'))

class Ponto:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    #__str__() menssagem bonitas para o usuário
    def __str__(self):
        return f'({self.x},{self.y})'
    
    #__repr__() funciona em parceira com eval que transforma str em operações
    def __repr__(self):
        return f'Ponto({self.x + 1}, {self.y + 1})'

p1 = Ponto(1,2)
p2 = eval(repr(p1))

print(p1)
print(p2)