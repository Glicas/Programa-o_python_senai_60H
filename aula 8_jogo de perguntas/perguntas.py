import random



banco_perguntas = [
'',
'Qual é o maior planeta do Sistema Solar?',
'Qual país tem o formato de uma bota?',
'Quantos continentes existem na Terra?'

]





respostas = [
'', 
'1- Jupiter',
'2- Italia',
'3- Sete'

]

print('jogo de perguntas e respostas e ganhe alguma coisa')
print('***' * 20)


maquina = random.choice(banco_perguntas)
id_maquina = banco_perguntas.index(maquina)
print(maquina)
print('***' * 20)

print('escolha sua resposta')
r = int(input(f'{respostas[1]} | {respostas[2]} | {respostas[3]}'))

if r == id_maquina:
    print('acetou fi')
else:
    print('errou')    



