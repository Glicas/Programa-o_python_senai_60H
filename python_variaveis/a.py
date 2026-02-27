print('sistema de média')
nome = input("digite o nome do aluno")


print('digite as notas do aluno',nome)
nota1 = float(input("digite nota1"))
nota2 = float(input("digite nota2"))
nota3 = float(input("digite nota3"))
print("")

print('***' * 15)

print('')

print('media da aluno(a)',nome)
media = (nota1 + nota2 + nota3) / 3
print(round(media),5)

aprovada = media >= 7
recuperacao = media >= 5 and media <7
reprovada = media <= 5

print(f'''
situação da aluno(a) {nome}
aprovada? - {aprovada}
reprovada? - {reprovada}
recuperação? - {recuperacao}

sua media - {media}

''')