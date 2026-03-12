pessoas = int(input("digite quantas pessoas tem para cadastrar"))
cadastro = []
idade = []
quartos = ['simples','duplo','luxo']
dia = []
estadia = []
pagamento = []

if pessoas == 1:
    cadastro = input('digite seu nome')
    idade = int(input('digite sua idade'))
elif pessoas == 2:
    cadastro = input('digite seu nome')
    idade = int(input('digite sua idade'))
    cadastro = input('digite seu nome')
    idade = int(input('digite sua idade'))
elif pessoas == 3:
    cadastro = input('digite seu nome')
    idade = int(input('digite sua idade'))
    cadastro = input('digite seu nome')
    idade = int(input('digite sua idade'))
    cadastro = input('digite seu nome')
    idade = int(input('digite sua idade'))
else:
    print('digite algo possivel de identificar')

print('')
print('---' * 20)
print('')

print ('escolha seu quarto: (1) simples: R$ 100,00 por dia, (2) duo: R$ 150,00 por dia,  (3) luxo: R$250,00 por dia')
escolha = int(input('digite o numero do quarto'))

if escolha == 1:
    dia = int(input('digite quantos dia irá ficar'))
    estadia = 100 * dia
if escolha == 2:
    dia = int(input('digite quantos dia irá ficar'))
    estadia = 150 * dia
if escolha == 3:
    dia = int(input('digite quantos dia irá ficar'))
    estadia = 250 * dia
else:
    print("digite algo plausível")

print('')
print('a sua estadia total é', estadia)
print('')
print('qual a forma de pagamento?')
print('(1) pix ,  (2) cartao debito ou (3) cartao credito')
pagamento = int(input("digite o pagamento"))

if pagamento == 1:
    print('pagamento concluido')
elif pagamento == 2:
    print('pagamento concluido')
elif pagamento == 3:
    print('pagamento concluido')
else:
    print('erro')    

print('')
resumo = int(input('deseja ver o resumo da compra? se sim (1) se não (2)'))

if resumo == 1:
    print(
print('total de pessoas',pessoas),
print(''),
print('nome',cadastro),
print(''),
print('idade: ',idade),
print(''),
print('escolha: (1) simples: R$ 100,00 por dia, (2) duo: R$ 150,00 por dia,  (3) luxo: R$250,00 por dia',escolha),
print(''),
print('quantidade de dias',dia),
print(''),
print('total de estadia:',estadia),
print(''),
print('pagamento:(1) pix ,  (2) cartao debito ou (3) cartao credito:',pagamento)
 )
elif resumo == 2:
    print('aproveito o quarto')
else:
    print('erro')