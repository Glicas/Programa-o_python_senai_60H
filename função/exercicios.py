#exercicio 1


def numero(): 
    o = int(input("digite um numero para ver se é impar ou par"))
    if o % 2 == 0:
          print('numero par')
    else:
        print('numero impar')
  

numero()

print('')

#exercicio 2

def multiplica():
    i = 3
    o = 90
    j = 30
    multiplicar = (i * o) * j
    print('resultado da multiplicação: ', multiplicar)

multiplica()

print('')

#exercicio 3

def elevado ():
    k = float(input('digite qual numero quer q seja elevado'))
    p = float(input('digite um numero'))
    elevado = k ** p
    print('resultado da elevação: ', elevado)
elevado()

print('')

#exercicio 4

def idade():
    i = int(input('digite sua idade'))
    if i == 18:
        print('parabéns, acabou de começar a fase adulta')
    else:
        print('nada')
idade()

print('')

#exercicio 5

def idade2():
    j = int(input('qual sua idade'))
    print('idade: ',j)
idade2()