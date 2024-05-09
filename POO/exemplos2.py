class Funcionario:
    
    def __init__(self, nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario
    
    def bonificacao(self):
        return self._salario * 0.1


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
    

g = Gerente('felipe', '111.111.111-11', 5000, '123', 0)
f = Funcionario('rivae','222.222.222-22', 4000)
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
    
    def __str__(self):
        return f'({self.x},{self.y})'
    
    def __repr__(self):
        return f'Ponto({self.x + 1}, {self.y + 1})'

p1 = Ponto(1,2)
p2 = eval(repr(p1))

print(p1)
print(p2)