#EXERCÍCIO 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
#EXERCÍCIO 108: Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.
#EXERCÍCIO 109: Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
#EXERCÍCIO 110: Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.
import moeda


p = int(input('Digite o preço: R$').strip())
t = int(input('Digite uma taxa: ').strip())
moeda.aumentar(p,t,format=True)
moeda.diminuir(p,t,format=True)
moeda.dobro(p,format=False)
moeda.metade(p,format=False)

print('~='*20)

#EXERCÍCIO 110: Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.
import moeda

p = int(input('digite um preço: R$').strip())
moeda.resumo(p,20,12)