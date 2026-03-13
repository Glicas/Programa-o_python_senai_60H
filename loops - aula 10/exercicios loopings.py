#atividade 1

#exercicio 1

n = 0

while n <= 100:
     print("Número:", n)
     n += 1

print('')
print('')

#exercicio 2

lista_nomes  = []
quantidade  =  int(input('Quantidade de pessoas'))

while quantidade > 0:
        nome = input("digite o nome")
        lista_nomes.append(nome)
        quantidade = quantidade - 1
        if quantidade <= 0:
               break
else:
  print("digite algo valido")
print('os nomes',lista_nomes)

print('')
print("")

#atividade 2

#exercicio 1

print('bem vindo')
note = []
mediaa = []
escola = {
'verificacao':{
'senha':'30',
'nome':'Gilberto'
},
'coisas_escolares':{
    'notas':[],
    'media':[]
},
}

for chances in range(3):
    print('Area escolar')
    senha  =  input('digite a sua senha: ')
    if senha == escola['verificacao']['senha']:
        print('Conta de ', escola['verificacao']['nome'])
        liberar = input('Deseja acessar o menu escolar? ')
        while liberar == 'sim':
            print('o que deseja acessar:', ' 1- notas | 2- media | 3- ver das medias resultado| 0 - sair')
            
            acesso = (int(input('acessar>>>>> ')))
            if acesso ==1:
                 print('notas')
                 n1 = float(input("digite a nota 1 "))
                 n2 = float(input("digite a nota 2 "))
                 n3 = float(input("digite a nota 3 "))
                 note.append(n1)
                 note.append(n2)
                 note.append(n3)
            elif acesso ==2:
                 mediaa = float(input('digite a media '))
                 resultado = (n1 + n2 + n3) / mediaa
                     
            elif acesso ==3:
                  print('notas:')
                  print('notas ',note)
                  print('media ',mediaa)
                  print('resultado da media ', resultado)
            elif acesso ==0:
                 print('ok')
                 break
            else:
                 print("digite algo valido")

else:
    print('conta bloqueada entre em contato com a escola')

input('digite enter para sair')      



      

 

