import os
import sys
import pandas as pd


def menu():
    print(' ')
    print('DIGITE O NUMERO CORRESPONDENTE A OPCAO DESEJADA')
    print(' ')
    print('1 - Adicionar novo comercial')
    print('2 - Vizualizar tabela')
    print('3 - Exlcluir entrada')
    print('4 - Mudar diretorio')
    menuop = int(input('>>>>'))
    return menuop


def path():
    diretorio = "diretorio.txt"
    os.path.isfile(diretorio)
    if os.path.isfile(diretorio):
        arquivo = open(diretorio, 'r+')
        texto = arquivo.readlines()
        mudar_diretorio = input(f"O diretorio atual e: {texto}, deseja mudar?")
        if mudar_diretorio.upper() == 'SIM':
            caminho = input("Digite onde onde será salvo os arquivos: ")
            arquivo = open(diretorio, 'w+')
            arquivo.write(caminho)
            arquivo.close()
            print("diretorio modificado")
            menuop
        elif mudar_diretorio.upper() == "NÃO":
            print("O diretorio atual não será mudado. retornando ao menu principal. ")
            menuop
        else:
            print("Opcao invalida, retornando ao menu")
            menuop
    else:
        arquivo = open(diretorio, 'w+')
        caminho = input("Digite onde seá salvo os arquivos. ")
        arquivo.writelines(caminho)
        os.system("attrib +h diretorio.txt")
        arquivo.close()
        print("diretorio salvo")


def cadastro():
    mes = input("Digite o mes: ")
    mes = mes.upper()
    arquivo = open('diretorio.txt', 'r+')
    texto = arquivo.read()
    mes = str(texto + "/" + mes)
    if os.path.isdir(mes):  # vemos de este diretorio ja existe
        print('Ja existe uma pasta com esse nome!')

    else:
        criar = input(f"não existe uma pasta para o mês em {mes}!, deseja criar? ")
        criar = criar.upper()
        if criar == "SIM":
            os.mkdir(mes)
            print(f"Foi criada uma pasta para o mês em {mes}!")
        elif criar == "NÃO":
            print("Retornando ao menu, pasta não será criada")
    vt: str = input("Digite o nome do VT: ")
    vt = vt.upper()
    novo_programa = input("Digite em qual programa: ")
    novo_programa = novo_programa.upper()
    while True:
        dias = input("Digite os dias: ")
        dias = dias.upper()
        if dias == "VOLTAR":
            print("voltando")
            break
        elif dias == "MUDAR":
            cadastro()
        else:
            print("Continuando")
            filename = (mes + "/" + dias + ".csv")
            os.path.isfile(filename)
            if os.path.isfile(filename):
                result = pd.read_csv(filename)  # read the csv file
                print(result.head())  # print result
                result.head(15)
                if novo_programa in result.head():
                    print("ja tem o programa")
                    result.tail(15)
                    if vt in result.tail():
                        print("ja tem o vt")
                    else:
                        print("não tem o vt, sera adicionado...")
                        print(result)
                        result.loc[-1, novo_programa] = vt
                        result.update(result.fillna('--'))
                        # saving the dataframe
                        result.to_csv(filename, index=False)
                        print(result.head())
                else:
                    print("não tem o programa na tabela sera adicionado")
                    result.loc[-1, novo_programa] = vt
                    result.update(result.fillna('--'))
                    print(result.head())
                    result.to_csv(filename, index=False)
            else:
                print("não existe tabela para o dia \n será criada uma tabela")
                programas = {' ': ['']}
                programas.setdefault(novo_programa, vt)
                df = pd.DataFrame.from_dict(programas)
                print(df)
                # saving the dataframe
                df.to_csv(filename, index=False)


def vizualizar():
    mes = input("Digite o mes: ")
    mes = mes.upper()
    arquivo = open('diretorio.txt', 'r+')
    texto = arquivo.read()
    mes = str(texto + "/" + mes)
    if os.path.isdir(mes):
        dias = input("Digite os dias vizualizar: ")
        filename = (mes + "/" + dias + ".csv")
        os.path.isfile(filename)
        if os.path.isfile(filename):
            result = pd.read_csv(filename)
            print(result)
        else:
            print("Não existe tabela para o dia inserido. Use a Opção 'Adicionar Comerciais' para criar a tabela")
    else:
        criar = input("Não existe uma pasta com o mês digitado, deseja criar? ")
        criar = criar.upper()
        if criar == "SIM":
            os.mkdir(mes)
            print(f"Foi criada uma pasta para o mês em {mes}!")
        elif criar == "NÃO":
            print("Retornando ao menu, pasta não será criada")
        else:
            print("Opção invalida, retornando ao menu. ")


while True:
    menuop = menu()
    if menuop == 1:
        cadastro()

    elif menuop == 2:
        vizualizar()

    elif menuop == 4:
        path()
