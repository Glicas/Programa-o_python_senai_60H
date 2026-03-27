import os


# Exercício 1: Criar e ler um Arquivo

#with open('testb.txt', 'w') as novo_arquivo: (para criar um novo arquivo text)
    #os.mkdir('novo_arquivo')


with open('abc.txt', 'r') as arquivo:
    conteúdo = arquivo.read()
    print(conteúdo)

    
# Renomeando o arquivo

#os.rename('testb.txt', 'abc.txt')
import shutil #('remove')
shutil.rmtree('c:/Users/aluno/Desktop/aula12/')


import shutil #('copia todo o diretorio')
shutil.copytree('abc', 'nome da copia')