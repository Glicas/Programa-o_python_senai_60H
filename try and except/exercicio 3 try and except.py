try:
    l = [123,5,3]
    print(l[7])
except IndexError:
    print('Esse indice não existe')
else:
    print('Erro sla')
finally:
    print('FIM ')