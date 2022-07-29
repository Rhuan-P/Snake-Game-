
#if pygame.key.get_pressed()[tecla] 
#(ao manter tecla pressionada. obs: não funcionando no celular)

import pygame
from pygame.locals import *
from sys import exit
from random import randint
pygame.init()



#variaveis de localização
alt = 720
larg = 720

y = larg/2
x = alt/2

x_m = randint(50,650)
y_m = randint(50, 650)

def spawn(R):
    
    R= randint(0,100)
   
    
    if R > 1:
        
        x_m = randint(50,650)
        y_m = randint(50, 650)
        
        
        

tam = 30
sp = 20

macas = 0
corpo = []
frame = 30
cobraSpeed = 10
xc = 0
yc = 0

#variaveis de apresentação
fonte = pygame.font.SysFont("arial",30, True,False)
tela= pygame.display.set_mode((larg, alt))
fps = pygame.time.Clock()
pygame.display.set_caption("GameTest by Mazonia")

def aumenta(corpo):
    for XeY in corpo:
        pygame.draw.rect(tela,(0,255,10),(XeY[0],XeY[1], 30,30))
while True:
    fps.tick(frame)
    tela.fill((0,0,0))
    
    
    string = f"maçãs: {macas} "
    mensage = fonte.render(string, False,(255,255,255))
    
#Fecha o game
    for event in pygame.event.get():
       
    
        if event.type == QUIT:
            pygame.quit()
            exit()
    
   #controles
        if event.type == KEYDOWN:
            
            if event.key == K_w :
                if yc == cobraSpeed:
                    pass
                else:
                    yc = -cobraSpeed
                    xc = 0
            if event.key == K_a :
                if xc == cobraSpeed:
                    pass
                else:
                    xc = -cobraSpeed
                    yc = 0
            if event.key == K_s :
                if yc == -cobraSpeed:
                    pass
                else:
                    yc = +cobraSpeed
                    xc = 0
            if event.key == K_d :
                if xc == -cobraSpeed:
                    pass
                else:
                    xc = +cobraSpeed
                    yc = 0
    x += xc
    y += yc
 #respawn parede
    if y > larg-50:
        y = 20
    if x > alt-50:
        x=20
    if x < 20:
        x = alt-50
    if y < 20:
        y = larg-50

   
   #spawn object
    cobra = pygame.draw.rect(tela,(0,255,10),(x,y,tam, 30))
    maca = pygame.draw.rect(tela,(255,0,0),(x_m,y_m,30,30))
    
    #grava corpo
    cabeça = []
    cabeça.append(x)
    cabeça.append(y)
    corpo.append(cabeça)
    if len(corpo) > macas:
        del corpo[0]
    
  #colisao
    if cobra.colliderect(maca):
        macas += 1
        frame += 3
        x_m = randint(50,650)
        y_m = randint(50,650)
        
    else:
        R= randint(0,200)
   
    
        if R == 100:
            
            x_m = randint(50,650)
            y_m = randint(50, 650)
        
        
        
        
        
    aumenta(corpo)
    
      
   
   
   
   
   
   
    tela.blit (mensage,(alt/2 - 20,0))
    pygame.display.updalte()    