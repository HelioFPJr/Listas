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
'''def ler_csv():
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
        print(f'Algo falhou: {fail}')'''

def teste_ler_csv():
    ler_csv2()

def ler_csv2():
    arquivo = 'csv/lista_num1.csv'
    try:
        with open(arquivo, 'r') as csvfile:
            dados = csv.reader(csvfile)
            lista = list(dados)
            print(f'\n{lista}')
            print(lista[0])
            print(lista[1])
            return lista
    except FileNotFoundError:
        print(f'Arquivo não encontrado: {arquivo}')
    except Exception as fail:
        print(f'Algo falhou: {fail}')

'''@pytest.mark.parametrize('num,num1',ler_csv())
def testar_tabuada_csv(num,num1):
    for i in num:
        print(num)
        for i2 in range(1,11):
            print(f'{num} X {i2} = {int(num)*i2} | {num1} X {i2} = {int(num1)*i2}')
            assert int(num)*i2 == int(num1)*i2'''

@pytest.mark.parametrize('lista',ler_csv2())
def testar_tabuada_csv2(lista):
    res2 = [['5', '10', '15', '20', '25', '30', '35', '40', '45', '50'], ['8', '16', '24', '32', '40', '48', '56', '64', '72', '80']]
    #res3 = ['8','16','24','32','40','48','56','64','72','80']
    #res2 = [5,10,15,20,25,30,35,40,45,50]
    #res3 = [8,16,24,32,40,48,56,64,72,80]
    assert lista == res2
    #assert lista == res3