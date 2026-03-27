import pygame

pygame.init()


tela = pygame.display.set_mode((500,500))
run = True


while run:
   for event in pygame.event.get():
        if event.type == pygame.QUIT:
         run = False
         pygame.quit()
     
   tela.fill((55,25,120))
   pygame.draw.rect(tela, ('#ffffff'), (235,235,30,30))
   pygame.display.update()
pygame.quit