import random

print('MegaSena!')
numeros = list(range(1,60))
quantos_numeros_deaposta = int(input('A partir de 6: '))

if quantos_numeros_deaposta == 6:
   
    n1 = random.choice(numeros)
    n2 = random.choice(numeros)
    n3 = random.choice(numeros)
    n4 = random.choice(numeros)
    n5 = random.choice(numeros)
    n6 = random.choice(numeros)

    lista_maquina = [n1,n2,n3,n4,n5,n6]
   
    m1 = int(input('Escolha de 1 à 60'))
    m2 = int(input('Escolha de 1 à 60'))
    m3 = int(input('Escolha de 1 à 60'))
    m4 = int(input('Escolha de 1 à 60'))
    m5 = int(input('Escolha de 1 à 60'))
    m6 = int(input('Escolha de 1 à 60'))
   
   
    minha = []
    if m1 in lista_maquina:
       minha.append(m1)
       if m2 in lista_maquina:
        minha.append(m2)
        if m3 in lista_maquina:
           minha.append(m3)
           if m4 in lista_maquina:
              minha.append(m4)
              if m5 in lista_maquina:
                 minha.append(m5)
                 if m6 in lista_maquina:
                    minha.append(m6)        
       
print('Seus acertos -  ', minha)
tamanhoMeu = len(minha)
tamanhoMaqui = len(lista_maquina)

   
print('acertou quantidade:', tamanhoMeu)                
print('seus numeros: ', [m1,m2,m3, m4, m5, m6,])