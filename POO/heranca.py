class Funcionario:
    
    def __init__(self, nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario
    #todas as def da class mãe(funcionario) seram herdadas nas outras classes, para que isso não aconteça basta criar a mesma def na class filhas.
    def bonificacao(self):
        return float(self._salario*(1+0.1))


class Gerente(Funcionario):
    
    def __init__(self, nome, cpf, salario, senha, qtd_funcionario):
        super().__init__(nome, cpf, salario)
        self._senha = senha
        self.qtd_funcionario = qtd_funcionario
    
    def autentica(self, senha):
        if self._senha == senha:
            print('Acesso permitido')
        else:
            print('Acesso negado')
    
    def bonificacao(self):
        print(f'seu salário com aumento fica {self._salario*(1+0.15)}')
        
    #Usando super().bonificacao() ira procuara a def bonificacao na class mae e utilizarar os return dela
    def bonificacao2(self):
        print(f'seu salário com aumento fica(super) {super().bonificacao() + 150}')
    
    def meu_nome(self):
        print(f'meu nome é {self._nome}')


class Diretor(Gerente):
    
    def __init__(self, nome, cpf, salario, senha, qtd_funcionario):
        super().__init__(nome, cpf, salario, senha, qtd_funcionario)
    
    def bonificacao(self):
        print(f'seu salário com aumento fica {self._salario*(1+0.2)}')
    
    #a Class Diretor vai hersar a def bonificacao de Gerente. Se não tivesse herdaria de Funcionarios
    def meu_nome(self):
        print(f'meu nome é {self._nome}')

c = Gerente('felipe', '111-111-111.11', 1250, 'f123', 1)
d = Diretor('dudu', '111.111.111-11', 4500, 'd123', 1)

c.meu_nome()
c.bonificacao()
c.bonificacao2()
d.meu_nome()
d.bonificacao()

print('-='*30)

#Algumas Curiosidades
class Ponto:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return (f'({self.x}, {self.y})')
    
    def __repr__(self):
        return (f'Ponto ({self.x + 1}, {self.y + 1})')


p1 = Ponto(1, 2)
p2 = eval(repr(p1))

print(p1)
print(p2)