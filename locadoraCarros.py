lista_carros = [
    {
        'carro': 'Chevrolet Taracker',
        'preco' : 120
    },
    {
        'carro': 'Chevrolet Onix',
        'preco' : 90
    },
    {
        'carro': 'Chevrolet Spin',
        'preco' : 150
    },
    {
        'carro': 'Hyundai HB20',
        'preco' : 85
    },
    {
        'carro': 'Hyundai Tucson',
        'preco' : 120
    },
    {
        'carro': 'Fiat Uno',
        'preco' : 60
    },
    {
        'carro': 'Fiat Mobi',
        'preco' : 70
    },
    {
        'carro': 'Fiat Pulse',
        'preco' : 130
    }
]

import os

carros_alugados = []

def menu():
    os.system('clear')
    print("=======================================")
    print("Bem vindo a locadora de carros!!")
    print("=======================================\n")


    print('O que deseja fazer ?\n')
    print('0 - Mostrar portifólio  |  1 - Alugar Carro  |  2 - Devolver Carro')
    op = int(input())

    if op == 0:
        portifolio()
    if op == 1:
        alugarCarro()
    if op == 2:
        devolverCarro()

def portifolio():
    os.system('clear')
    visualizarCarros()

    print('\n==========')
    print('0 - Continuar | 1 - Sair')
    op = int(input())
    continuarSair(op)

def alugarCarro():
    os.system('clear')
    print('[ ALUGAR ] Dê uma olhada em nosso portifolio')
    visualizarCarros()

    print('\nEscolha o código do carro:')
    cd_carro = int(input())
    print('Escolhas quantos dias deseja ajugar: ')
    dias_alugar = int(input())

    for index, carro in enumerate(lista_carros):
        if cd_carro == index:
            print(f"Você escolheu o {carro['carro']} por {dias_alugar} dias")
            total_aluguel = carro['preco'] * dias_alugar
            print(f'O Alugel totalizará R${total_aluguel}. Deseja Alugar?')

            print('\n0 - SIM | 1 - NÃO')
            op = int(input())

            if op != 0:
                print(f'Você desistiu de alugar...')
                return

            carro_alugado = lista_carros.pop(index)
            carros_alugados.append(carro_alugado)
            print(f"\nParabéns você alugou o {carro['carro']} por {dias_alugar} dias")
            menu()

def devolverCarro():
    os.system(('clear'))
    print('Segue a lista de carros alugados. Qual você deseja devolver?')
    for index, carro in enumerate(carros_alugados):
        print(f"[{index}] {carro['carro']} - R$ {carro['preco']} / dia")

    print('Escolha o código do carro para devolver: ')
    cd_carroDev = int(input())
    for index, carro in enumerate(carros_alugados):
        if cd_carroDev == index:
            carro_devolver = carros_alugados.pop(index)
            lista_carros.append(carro_devolver)
    menu()

def visualizarCarros():
    carros_com_indices = [f"[{index}] {carro['carro']} - R$ {carro['preco']} /dia" for index, carro in enumerate(lista_carros)]
    for carro_info in carros_com_indices:
        print(carro_info)

def continuarSair(op):
    if op == 0: 
        menu()
    return

menu()