import abc

class Autentica(abc.ABC):
    """Classe abstrata que contém operações	de um objeto autenticável. As subclasses concretas devem sobrescrever o método autentica
	"""
    #Métado abstrato que faz verificação da senha. devolve True se a senha confere e False o oposto
    @abc.abstractmethod
    def autentica(sel, senha):
        """	Método abstrato	que	faz	verificação da senha. Devolve True se a senha confere, e False caso contrário.
        """


class Gerente:
    
    def __init__(self, nome, cpf, salario, qtd_funcionario = 0):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario
        self.qtd_funcionario = qtd_funcionario
    
    def autentica(self, senha):
        ...
    
    def bonificacao(self):
        return self._salario*(0.15)

#é isso que é interface uma herança que não chamada na class
Autentica.register(Gerente)

g = Gerente('fel', '222.222.222-22',3000)


#EXEMPLO
class Tributavel(abc.ABC):
    
    @abc.abstractmethod
    def valor_imposto(self):
        ...


class Conta:
    
    def __init__(self, nome, cpf, saldo):
        self._nome = nome
        self._cpf = cpf
        self._saldo = saldo


class Contacorrente(Conta):
    
    def __init__(self, nome, cpf, saldo):
        super().__init__(nome, cpf, saldo)
    
    def valor_imposto(self):
        return self._saldo * 0.01


class Seguro:
    
    def __init__(self, valor, titular, numero_apolice):
        self._valor = valor
        self._titular = titular
        self._numero_apolice = numero_apolice
    
    def valor_imposto(self):
        return 50 + self._valor * 0.05


class Manipulador:
    
    def calcula_imposto(self, lista_tributaveis):
        total = 0
        for t in lista_tributaveis:
            if isinstance(t, Tributavel):
                total += t.valor_imposto()
            else:
                print(t.__repr__(), "não é tributavel")
        return total


cc = Contacorrente('fel', '111.111.111-11', 5000)

s = Seguro(250, 'felipe', '123-77')

Tributavel.register(Contacorrente)
Tributavel.register(Seguro)

list_tributos = [cc, s]

m = Manipulador()
total = m.calcula_imposto(list_tributos)
print(total)