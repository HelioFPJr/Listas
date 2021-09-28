import pytest
#num1 = int(input('Qual a quantidade de caixa de fosforo? '))
num1 = 10
print(f'O numero escolhido foi: {num1}')
print('Lembrete: A caixa contém 40 palitos')
num2 = 40
def calcular_fosforos(num1,num2):
    return num1 * num2
print(f'O numero total de palitos é: {calcular_fosforos(num1,num2)}')

#===========================================================================
res = []
#num = int(input('Qual o numero que deseja fazer a tabuada? '))
num = 10
def tabuada():
    #num = 2
    print(f'O numero escolhido foi: {num}')
    for i in range(11):
        print(f'{num} x {i} = {num*i}')
        res.insert(i,num*i)
    print(res)
tabuada()


def teste_fosforos():
    num1 = 10
    num2 = 40
    resultado_esperado = 400
    resultado_atual = calcular_fosforos(num1,num2)
    assert resultado_esperado == resultado_atual

def teste_tabuada():
    res2 = []
    num = 2
    for i in range(11):
        print(f'{num} x {i} = {num * i}')
        res2.insert(i,num*i)
    print(res)
    print(res2)
    for i in range(11):
        assert res[i:11] == res2[i:11]
    