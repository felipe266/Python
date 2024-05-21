import abc


class Funcionario(abc.ABC):
    
    def __init__(self, nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario

    #Ao adicionar @abc.abstractclassmethod todas as class filhas serão obrigadas a herda essa def
    @abc.abstractclassmethod
    def bonificacao(self):
        return float(self._salario*(0.1))


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
        return self._salario*(0.15)


class Diretor(Funcionario):
    def __init__(self, nome, cpf, salario, senha):
        super().__init__(nome, cpf, salario)
        self._senha = senha
        
    def autentica(self, senha):
        if self._senha == senha:
            print('acesso permitido')
        else:
            print('acesso negado')
    
    def bonificacao(self):
        return self._salario*(0.2)

#isso é polimorfismo é uma class que recebe valores de de outras class sem a necessidades de mudanção para futuras outras class
class ControleBonificacao:
    
    def __init__(self, total_bonificacao=0):
        self._total_bonificacao = total_bonificacao
    
    def registra(self, funcionario):
        try:
            self._total_bonificacao += funcionario.bonificacao()
        except AttributeError as e:
            print(e)
    
    def total_bonificacao(self):
        return self._total_bonificacao


g = Gerente('ipe', '222.222.222-22', 5000, 'f123', 0)

d = Diretor('fel', '111.111.111-11', 5000, 'f123')

controle = ControleBonificacao()
controle.registra(g)
controle.registra(d)

print(f'total: {controle.total_bonificacao()}')