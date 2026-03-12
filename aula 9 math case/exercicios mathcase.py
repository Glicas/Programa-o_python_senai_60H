#exercício 1

numero = int(input('digite numero'))

match numero:
    case numero if numero % 2 == 0:
        print('par')
    case numero if numero %2 == 1:
        print('impar')


print('')
print('')

#exercicio 2

number = int(input('digite o number'))

match number:
    case number if number >= 1:
        print('numero positivo')
    case 0:
        print('zero')
    case number if number <= -1:
        print('numero negativo')
    
print("")
print("")

#exercício 3
a = input('digite algo')
match a:
    case '':
        print('vazio')
    case  _:
        print('preenchido')
print('')
print("")

#exercicio 4

oi = int(input('digite numero'))

match oi:
    case oi if oi > 10:
        print('maior que 10')
    case 10:
        print('igual a 10')
    case oi if oi < 10:
        print('menor que 10')

print('')
print('')

#exercicio 5

idade = int(input('digite a idade'))

match idade:
    case idade if idade >= 35 and idade < 64:
        print('adulto')
    case idade if idade <=35 and idade > 17:
        print('jovem')
    case idade if  idade <= 17 and idade > 12:
        print('adolescente')
    case idade if idade <= 12:
        print('criança')