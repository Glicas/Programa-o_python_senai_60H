def cumprimento(nome):
    return 'olá', nome

def produto(lista_prod, prod, carrinho, meus_v, lista_valores, paga):

    carrinho.append(lista_prod[prod])
    meus_v.append(lista_valores[paga])
    return carrinho,'R$',  float(sum(meus_v))


def pagamento(lista_tip_pags, escolha_pag):
    return lista_tip_pags[escolha_pag]




def restaurante():
   
    menu = ['','SALADA', 'MACARRONADA', 'SANDUICHE', 'SORVETE']
    valores  = [0,100,60,150,250]
    carrinho = []
    meus_valores = []
    nome = input('Nome: ')
    print(cumprimento(nome))
 
    for p, v in enumerate(zip(menu, valores)):
        print(p,'R$', v)    

    acrescentar =  input('deseja acrescentar ao carrinho? ')
    while acrescentar == 'sim':    
        e  =  int(input('Escolha seu produto: 1 ,2 ,3, 4'))
        print( produto(menu, e, carrinho, meus_valores,valores, e ))
        acrescentar = input('Deseja continuar? ')
 
    else:
        lista_pag = ['', '1 pix', '2 CC', ' 3 CD']
        escolha =  int(input(f'Escolha a forma de pagamento,  {lista_pag}'))
        print(pagamento(lista_pag, escolha))
        print('Obrigado volte SEMPRE!')    




restaurante()






# variavel global
nome = 'Carlos'
print(nome)

def mostrar_nome():
    # esta dentro da função
    nome  =  'Julia'
    print(nome)

def mostrar_nome2():
    print(nome)

print(nome)
mostrar_nome()
mostrar_nome2()

def mostrar_nome3():
    global nome, idade
    nome  =  'carlos'
    idade  =  25
    print(nome, idade)

print(nome)
mostrar_nome3()