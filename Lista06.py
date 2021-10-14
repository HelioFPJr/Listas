import pytest


#qtcx = int(input('Qual a quantidade de caixa de fosforo? \n'))
qtcx = 10
print(f'O numero escolhido foi: {qtcx}')
print('Lembrete: A caixa contém 40 palitos')

def calcular_fosforos(qtcx):
    return qtcx * 40
print(f'O numero total de palitos é: {calcular_fosforos(qtcx)}')

#===========================================================================
res = []
#tabu = int(input('Qual o numero que deseja fazer a tabuada? \n'))
tabu = 3
def tabuada():
    #tab = 2
    print(f'O numero escolhido foi: {tabu}')
    for i in range(11):
        print(f'{tabu} x {i} = {tabu*i}')
        res.insert(i,tabu*i) #armazena o resultado da tabuada na lista res2[] na posição i, o valor de num*i
    print(res)
tabuada() #mostra tabuada

def teste_fosforos():
    num1 = 10
    num2 = 40
    resultado_esperado = 400
    resultado_atual = calcular_fosforos(qtcx)
    assert resultado_esperado == resultado_atual

def teste_tabuada():
    res2 = []
    num = 8
    for i in range(11):
        #print(f'{num} x {i} = {num * i}') #mostrar que a tabuada ta sendo feita
        res2.insert(i,num*i) #armazena o resultado da tabuada na lista res2[] na posição i, o valor de num*i
    print(f'\n{res2} = {res}')
    for i in range(11): # faz o assert item por item das listas
        assert res[i:11] == res2[i:11]
