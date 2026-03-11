import random

maquina = ['','✂️','🪨','🧻']

escolha_maquina = random.choice(maquina[1:])
id_maquina = maquina.index (escolha_maquina)
minhas = [ '','✂️','🪨','🧻']

print("escolha '✂️ - 1' , '🪨 - 2' , '🧻 - 3' ")

minha_escolha = int(input('escolha o objeto'))

if minha_escolha == id_maquina:
    print('empate')
    print(escolha_maquina)
    print(minhas[minha_escolha])
elif id_maquina == 1 and minha_escolha == 3:
    print("vitoria da maquina!")
    print('minha escolha:',minha_escolha)
    print('escolha da maquina:', escolha_maquina)
elif id_maquina == 2 and minha_escolha == 1:
    print("vitoria da maquina!")
    print('minha escolha:',minha_escolha)
    print('escolha da maquina:', escolha_maquina)
elif id_maquina == 3 and minha_escolha == 2:
    print("vitoria da maquina!")
    print('minha escolha:',minha_escolha)
    print('escolha da maquina:', escolha_maquina)
elif minha_escolha == 1 and id_maquina == 3:
    print("sua vitoria")
    print('minha escolha:',minha_escolha)
    print('escolha da maquina:', escolha_maquina)
elif minha_escolha == 2 and id_maquina == 1:
    print("sua vitoria")
    print('minha escolha:',minha_escolha)
    print('escolha da maquina:', escolha_maquina)
elif minha_escolha == 3 and id_maquina == 2:
    print("sua vitoria")
    print('minha escolha:',minha_escolha)
    print('escolha da maquina:', escolha_maquina)
else:
    print('erro')