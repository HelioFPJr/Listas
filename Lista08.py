import pytest
import requests
import json

url = 'https://petstore.swagger.io/v2/pet'

def testar_incluir_pet():
    #configura
    headers = {'content-Type': 'application/json'}
    status_code_esperado = 200      #comunicação
    #executa
    resposta = requests.post(url,
                             data=open('json/pet.json','rb'),
                             headers = headers)
    print(resposta)
    print(resposta.status_code)
    print(json.dumps(resposta.json(),indent=2))

    #valida
    assert resposta.status_code == status_code_esperado

def testar_consultar_pet():
    #configura
    headers = {'content-Type': 'application/json'}
    pet_id = 16614
    cat_name_esperado = {'id': 0, 'name': 'Dog'}
    pet_name_esperado = 'Amy'
    tags_name = [{'id': 0, 'name': 'SRD'}]
    status_esperado = 'available'
    status_code_esperado = 200


    #executa
    resposta = requests.get(f'{url}/{pet_id}',headers=headers)
    corpo_da_resposta = resposta.json()
    print(corpo_da_resposta)
    print(resposta.status_code)
    print(json.dumps(resposta.json(), indent=2))

    #valida
    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['category'] == cat_name_esperado
    assert corpo_da_resposta['name'] == pet_name_esperado
    assert corpo_da_resposta['tags'] == tags_name
    assert corpo_da_resposta['status'] == status_esperado

def testar_alterar_pet():
    # configura
    headers = {'content-Type': 'application/json'}
    status_code_esperado = 200  # comunicação
    # executa
    resposta = requests.post(url,
                             data=open('json/pet1.json', 'rb'),
                             headers=headers)
    print(resposta)
    print(resposta.status_code)
    print(json.dumps(resposta.json(), indent=2))

    # valida
    assert resposta.status_code == status_code_esperado

def testar_excluir_pet(): # a API possui im key, mas cosigo deletar o pet sem ela
    # Configura
    headers = {'Content-Type': 'application/json'}
    pet_id = '16614'
    status_code_esperado = 200  # comunicação

    # Executa
    resposta = requests.delete(f'{url}/{pet_id}', headers=headers)

    # Valida
    assert resposta.status_code == status_code_esperado
