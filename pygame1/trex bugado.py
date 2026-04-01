# t-rex 

import random
import pygame
import sys

pygame.init()
largura = 800
altura  = 600
tela = pygame.display.set_mode((largura, altura))

# carregar img

trex1 =  pygame.image.load('assets/1.png')
trex2 =  pygame.image.load('assets/2.png')
trex3 =  pygame.image.load('assets/3.png')

cacto_img1 = pygame.image.load('assets/cacto.png')
cacto_img2 = pygame.image.load('assets/cacto2.png') 

chao =  pygame.image.load('assets/ground.jpg')

trex_x  = 100
trex_y  = 300

chao_x =  0

vel_y =  0
gravidade = 1
pulando  =  False

cacto_x  = 800
cacto_y  = 300
frame = 0
score  =  0
fonte  =  pygame.font.SysFont('Arial', 30)
game_over  =  False

clock = pygame.time.Clock()


while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.KEYDOWN:    
            if evento.key == pygame.K_SPACE and not pulando:
                vel_y = - 21
                pulando = True  

            if evento.key == pygame.K_k and game_over:
                trex_y = 300
                cacto_x = 800
                score = 0
                game_over =  False
    if not game_over:
        # gravidade
        vel_y += gravidade
        trex_y += vel_y           
        if trex_y >= 300:
            trex_y = 300
            pulando = False
        # chao infinito
        chao_x -= 5
        if chao_x <= -800:
           chao_x = 0     

        cacto_x  -= 5
        if cacto_x < -50:
            cacto_x = random.randint(800,1000)
            score += 1

        # frame
        frame += 1
        if frame > 20:
            frame = 0
        if frame <= 10:
            trex =  trex1
        elif frame > 10 and frame <=15:
             trex =  trex2
        else :
             trex = trex3                  

        trex_rect = trex.get_rect(topleft = (trex_x , trex_y))
        cacto_rect =  cacto_img1.get_rect(topleft = (cacto_x, cacto_y))
        cacto_rect2 =  cacto_img2.get_rect(topleft = (cacto_x, cacto_y))
        
        
        if trex_rect.colliderect(cacto_rect):
            if trex_rect.colliderect(cacto_rect2):
               game_over = True

    tela.fill('yellow')
    
    tela.blit(chao,(chao_x, 340)) 
    tela.blit(chao,(chao_x+800,340))
    tela.blit(trex, (trex_x, trex_y)) 
    tela.blit(cacto_img1, (cacto_x, cacto_y))
    tela.blit(cacto_img2, (cacto_x, cacto_y))

    # pontuação

    texto = fonte.render('Pontuação: '+ str(score), True, (0,0,0))
    tela.blit(texto, (650,30))      

    if game_over:
        texto2  =  fonte.render('game over aperte K ', True, (255,0,0))
        tela.blit(texto2, (250,200))
    pygame.display.update()
    clock.tick(30)    