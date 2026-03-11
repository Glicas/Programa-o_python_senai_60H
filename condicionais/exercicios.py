#exercício 2

idade = int(input('digite sua idade'))

if idade >= 16:
    print('você pode votar')
    print('deseja votar em lula ou bolsonaro')
    voto = input('deseja votar em quem')
    if voto == 'lula' or 'bolsonaro':
        print('parabéns você conseguiu votar aqui está em quem você votou', voto)
else:
    print('você não pode votar')

print("")
print('***' * 20)  

#exercício 3

sla = float(input('digite um número e veja se ele é par ou não'))

if sla % 2 == 0:
    print('numero par')
else:
    print('número impar')

    
print("")
print('***' * 20)  

#exercício 4

n1 = float(input('digite n1'))
n2 = float(input('digite n2'))
n3 = float(input('digite n3'))

if n1 >= n2 >= n3:
    print('triangulo equilatero')
elif n1 != n2 != n3:
    print('escaleno')
elif n1 != n2 >= n3:
    print('isosceles')
elif n1 >= n2 != n3:
    print ('isosceles')
else:
    print('erro')    


print("")
print('***' * 20)  

#exercício 5

m = float(input('digite o numero'))

if m %5 and m %7 == 0:
    print('numero é multiplo')
else:
    print('não é')

print("")
print('***' * 20)  

#exercício 6

numero = int(input('digite numero'))
positivo = True
if numero >= 10 and positivo and numero >= 0 :
    print('numero é positivo e é maior que 10')
else:
    print('nah id win')

print("")
print('***' * 20)  

#exercício 7


aaaaa = float(input('sigite o numeroooo'))


if aaaaa %3 == 0 and aaaaa %5 == 0:
    print('numero é divisivel')
else:
    print('subuxa')