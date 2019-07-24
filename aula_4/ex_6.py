
import os
import sys
import subprocess


current_module = os.path.abspath(os.path.curdir)
sys.path.append(current_module)

for f in os.listdir(current_module):
    print(f)

def gerar_csv(lista_de_dicionarios):

    arquivo = open('carol.csv', 'w')

    cabecalho = ';'.join(
        key.upper() for key in lista_de_dicionarios[0].keys()
    )
    arquivo.write(cabecalho + '\n')

    for dicionario in lista_de_dicionarios:
        linha = ';'.join(
            value for value in dicionario.values()
        )
        arquivo.write(linha) 

    arquivo.close()
