e_commerce = {
    'tenis':600.0,
    'fone' :50.0,
    'celular':1500.0
    }

print(e_commerce)

carrinho = []
valores =  []

produto_1 = input("digite produto 1 ")
produto_2 = input("digite produto 2 ")

carrinho.append(produto_1)

carrinho.append(produto_2)
print(carrinho)

valores.append(e_commerce[produto_1])
valores.append(e_commerce[produto_2])

print('R$', valores)
somar  =  sum(valores)
print('R$', somar)