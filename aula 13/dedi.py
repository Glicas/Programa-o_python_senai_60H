import random

def ex3():
    n   =  random.randrange(10,30)
    print(n)
    
ex3()

def ex4():
  for i in range (10,0,-1):
     print(i)
     if i == 1:
      print('Fogo!')
ex4()

print('')

def ex5():
   g = int(input('digite quantas tentativas deseja: '))
   for i in range(g):
      n1 = int(input('digite um numero par: '))
      n2 = int(input('digite outro numero par: '))
      if n1 % 2 == 0 and n2 % 2 == 0:
         resultado = n1 + n2
         print('resultado da soma: ', resultado)
         break
      else:
         print('digite algo válido')


ex5()

def ex6():
   g = int(input('digite um numero para saber a tabuada dele: '))
   for g in range(10,0,-1):
      
      resultado = g + g
      print(resultado)


ex6()

print('')

def ex7():
   for i in range (99,0,-2):
      print (i)

ex7()