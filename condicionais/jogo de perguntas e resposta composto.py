import random

banco_perguntas = [
'carregue novamente',
'O que é que tem cidades, mas não tem casas; tem montanhas, mas não tem árvores; e tem água, mas não tem peixes?',
'O que é que, quanto mais a gente tira, maior fica?',
'Por que um homem que vive em Nova York não pode ser enterrado na Califórnia?',
'O que é que tem dentes, mas não consegue morder?',
'Um agricultor tem 17 ovelhas. Todas, menos 9, morrem. Quantas ficam vivas?',
'O que é que quebra quando se fala?',
'O que é que tem cabeça, tem dentes, não é bicho e nem gente?',
'Qual é a pergunta que você nunca pode responder com "sim"?',
'O que é que cai em pé e corre deitado?',
'O que tem cinco dedos, mas não tem unhas?',
'Pergunta: Qual país tem o formato de uma bota?',
'Pergunta: Quantos continentes existem na Terra?'
]
respostas = [
'',
'1 Resposta: O mapa.',
'2 Resposta: O buraco.',
'3 Resposta: Porque ele ainda está vivo.',
'4 Resposta: O pente.',
'5 Resposta: Nove.',
'6 Resposta: O segredo.',
'7 Resposta: O alho ou o pente',
'8 Resposta: "Você está dormindo?',
'9 Resposta: A chuva.',
'10 Resposta: A luva.',
'11 Resposta: Italia',
'12 Resposta: Sete',
]

print('JOGO DE PERGUNTAS ACERTE E GANHE 1 MILHÃO')
print('***' * 20)
maquina  =  random.choice(banco_perguntas)
id_maquina =  banco_perguntas.index(maquina)
print(maquina)
print('***' * 20)

print('ESCOLHA SUA RESPOSTA')
r = int(input(f'''
{respostas[1]} , {respostas[2]} , {respostas[3]}
{respostas[4]} , {respostas[5]} , {respostas[6]}
{respostas[7]} , {respostas[8]} , {respostas[9]}
{respostas[10]} , {respostas[11]} , {respostas[12]}
                        
'''))

if r == id_maquina:
    print('acertou em cheio')
    print('A sua resposta é', respostas[r])
else:
    print('Errou feio')
    print('A sua resposta é', respostas[r])
    print('A resposta corrta é ', respostas[id_maquina] )

# else ou elif

print(r)
print(id_maquina)