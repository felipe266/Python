class teste():
    def fib(n):
        if n == 0 or n == 1:
            return n
        return teste.fib(n-1) + teste.fib(n-2)
    

    def dic(**vari):
        for k, v in vari.items():
            print(f'{k}: {v}')


    def par_impa(i, f):
        if i < f:
            for n in range(i,f+1):
                if n%2 == 0:
                    print(f'O {n} é par')
                    continue
                print(f'o {n} é impar')
        if i > f:
            for n in range(f,i+1):
                if n%2 == 0:
                    print(f'O {n} é par')
                    continue
                print(f'o {n} é impar')
    
    
    def soma(n = 0, b = 0) -> int:
        return n + b
 

print(teste.soma.__annotations__)
#declara o tipo do retorno da função
print(teste.fib(6))
print('~~'*10)
vari = teste.dic(nome = 'felipe', idade = 21, email = 'felipe@felipe')
print('~~'*15)
vari = teste.dic(**{'nome':'felipe', 'idade': 21, 'email':'felipe@felipe'})
print('~~'*15)
teste.par_impa(10,5)
print('~~'*15)
#--------------------------------------------------------------------------
#OBS: dentro de uma class só renotornam valores dentro de uma def
#--------------------------------------------------------------------------
class Conta:
    def __init__(self,numero, titular, saldo, limite) -> str:
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
    
    def depositar(self, valor):
        self.saldo += valor
        

conta = Conta(123-4, 'felipe', 1200, 2000)
conta.depositar(200)
print(conta.saldo)