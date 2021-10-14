import pytest
import csv


# teste parametrizado
@pytest.mark.parametrize('num,res', [
    # valores
    (5, [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]),  # teste 1
    (3, [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30]),  # teste 2
])
def testar_tabuada_parametrizada(num, res):
    for i in range(11):
        print(f'\n{num * i} = {res[i]}')  # mostra a assertiva
    for i in range(11):
        assert num * i == res[i]


# teste com csv
def ler_csv():
    lista_res_cvs = []
    arquivo = 'csv/lista_num.csv'
    try:
        with open(arquivo, newline='') as csvfile:
            dados = csv.reader(csvfile, delimiter=',')
            #next(dados)  # pular a primeira linha
            for i in dados:
                lista_res_cvs.append(i)
            print(lista_res_cvs)
            return (lista_res_cvs)

    except FileNotFoundError:
        print(f'Arquivo não encontrado: {arquivo}')
    except Exception as fail:
        print(f'Algo falhou: {fail}')

def teste_ler_csv():
    ler_csv2()

'''def ler_csv2():
    lista_res_cvs2 = []
    arquivo = 'csv/lista_num1.csv'
    try:
        with open(arquivo, newline='') as csvfile:
            dados = csv.reader(csvfile, delimiter=',')
            #next(dados)  # pular a primeira linha
            for i in dados:
                lista_res_cvs2.append(i)
            print(lista_res_cvs2)
            return lista_res_cvs2

    except FileNotFoundError:
        print(f'Arquivo não encontrado: {arquivo}')
    except Exception as fail:
        print(f'Algo falhou: {fail}')'''

@pytest.mark.parametrize('num,num1',ler_csv())
def testar_tabuada_csv(num,num1):
    for i in num:
        print(num)
        for i2 in range(1,11):
            print(f'{num} X {i2} = {int(num)*i2} | {num1} X {i2} = {int(num1)*i2}')
            assert int(num)*i2 == int(num1)*i2

'''@pytest.mark.parametrize('n1,n2,n3,n4,n5,n6,n7,n8,n9,n10',ler_csv2())
def testar_tabuada_csv2(n1,n2,n3,n4,n5,n6,n7,n8,n9,n10):
    res=[]
    for i in (1,2):
        print(i)
        for i2 in range(1,11):
            print(f'{n1} X {i2} = {int(n1)*i2}')
            res.append(int(n1)*i2)
        print(res)
    assert res == ler_csv2()'''