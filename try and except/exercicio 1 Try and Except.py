try:
    f = int(input("digite numero"))
except ValueError:
    print('erro no valor')
except TypeError:
    print('erro no calculo')    
else:
    print('Erro que não se conhece')
finally:
    print('Fim')