try:
    a = int(input('digite n1'))
    b = int(input('digite n2'))
    resultado = (a + b) / 0
except ZeroDivisionError:
    print('A divisão não pode ser por zero')
except TypeError:
    print('Dados no calculo aritmetico incorreto')  
except ValueError:
    print('Valor inserido incorretamente')  
else:
    print('Erro desconhecido')
finally:
    print('FIM')