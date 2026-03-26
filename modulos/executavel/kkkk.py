import random 



def verificar():
    
    print('ESCOLA: ')

    frequencia  =  [10,9,8,1,0,5,8,9,10,0]
    print('media')
    media1 =  media(frequencia)
    print(media1)
    print('mediana')
    mediana1 = mediana(frequencia)
    print(mediana1)
    print('moda')
    moda1 = moda(frequencia)
    print(moda1)
    print('Desvio padrão')
    desvio1 = desvio(frequencia)
    print(desvio1)

    print('menor nota')
    menor_nota(frequencia)
    print('maior nota')
    maior_nota(frequencia)


verificar()

    
#
    

    
    
import statistics


def moda(frequencia):
    moda1 = statistics.mode(frequencia)
    return moda1


def media(frequencia):
    media1 = statistics.mean(frequencia)
    return media1



def mediana(frequencia):
    mediana1 = statistics.median(frequencia)
    return mediana1


def menor_nota(frequencia):
    menor = min(frequencia)
    print(menor)

def maior_nota(frequencia):
    maior = max(frequencia)
    print(maior)


def desvio(frequencia):
    desvio1 = statistics.stdev(frequencia)
    return desvio1
