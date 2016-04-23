#! /usr/bin/python
# 1 - Library
import pygame
from pygame.locals import *
import math
import random

# 2 - Init
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Crazy Rabbit")
keys = [False,False,False,False]    # W A S D
player_pos = [150,150]
acc = [0,0]     #acc[0]/acc[1]  rate of successfully kill
arrows = []
badtimer=100
badtimer1=0
badguys=[[640,100]]
health_value=194

# 3 - Load
# 3.1 pictures
player = pygame.image.load("images/dude.png")
grass = pygame.image.load("images/grass.png")
castle = pygame.image.load("images/castle.png")
arrow = pygame.image.load("images/bullet.png")
badguyimg1=pygame.image.load("images/badguy.png")
badguyimg=badguyimg1
healthbar=pygame.image.load("images/healthbar.png")
health=pygame.image.load("images/health.png")
gameover=pygame.image.load("images/gameover.png")
youwin=pygame.image.load("images/youwin.png")

#3.2 mid
hit = pygame.mixer.Sound("audio/explode.wav")
shoot = pygame.mixer.Sound("audio/shoot.wav")
enemy = pygame.mixer.Sound("audio/enemy.wav")
hit.set_volume(0.05)
shoot.set_volume(0.05)
enemy.set_volume(0.05)
pygame.mixer.music.load("audio/moonlight.wav")
pygame.mixer.music.play(-1,0.0)
pygame.mixer.music.set_volume(0.20)

#4 - main loop
running=1
exitcode=0
while running:
    badtimer-=1

    #5 - clear the screen
    screen.fill(0)  

    #6 - pos the object    letf-up 
    #6.1
    for x in range(width/grass.get_width()+1):
        for y in range(height/grass.get_width()+1):
            screen.blit(grass,(x*100,y*100))

    screen.blit(castle,(0,30))
    screen.blit(castle,(0,130))
    screen.blit(castle,(0,240))
    screen.blit(castle,(0,345))

    #screen.blit(player,player_pos)   
    postion = pygame.mouse.get_pos()
    angle = math.atan2(postion[1]-(player_pos[1]+32),postion[0]-(player_pos[0]+32))
    player_rot = pygame.transform.rotate(player,360-angle*57.29)
    player_pos1 = (player_pos[0]-player_rot.get_rect().width/2,player_pos[1]-player_rot.get_rect().height/2)
    screen.blit(player_rot,player_pos1)

    

    #6.2 draw arrows
    for bullet in arrows:
        index=0
        velx=math.cos(bullet[0])*10
        vely=math.sin(bullet[0])*10
        bullet[1]+=velx
        bullet[2]+=vely
        if bullet[1]<-64 or bullet[1]>640 or bullet[2]<-64 or bullet[2]>480:
            arrows.pop(index)
        index+=1;
        for projectile in arrows:
            arrow1 = pygame.transform.rotate(arrow,360-projectile[0]*57.29)
            screen.blit(arrow1,(projectile[1],projectile[2]))

    #6.3 draw badguys
    if badtimer == 0:
        badguys.append([640,random.randint(50,430)])
        #print badguys
        badtimer = 100-(badtimer1*2)
        if badtimer1 >= 25:
            badtimer1=25
        else:
            badtimer1+=5
    index=0
    for badguy in badguys:
        if badguy[0]<-64:
            badguys.pop(index)
        badguy[0]-=5
        #attack casstle
        badrect=pygame.Rect(badguyimg.get_rect()) 
        badrect.top=badguy[1]
        badrect.left=badguy[0]
        if badrect.left<64:
            hit.play()
            health_value-=random.randint(5,20)
            badguys.pop(index)
        #kill the badguys
        index1=0
        for bullet in arrows:
            bullrect=pygame.Rect(arrow.get_rect())
            bullrect.left=bullet[1]
            bullrect.top=bullet[2]
            if badrect.colliderect(bullrect):   #judge cross
                enemy.play()
                acc[0]+=1
                badguys.pop(index)
                arrows.pop(index1)
            index1+=1
        #next badguy
        index+=1
    #print badguys[0]
    for badguy in badguys:
        screen.blit(badguyimg,badguy)

    #6.4 draw clock
    font = pygame.font.Font(None,36)
    survivedtext=font.render(str((60000-pygame.time.get_ticks())/60000)+":"+str((60000-pygame.time.get_ticks())/1000%60).zfill(2), True, (0,0,0))
    textRect = survivedtext.get_rect()
    textRect.topright = [635,5]
    screen.blit(survivedtext,textRect)

    #6.5 draw healthbar
    screen.blit(healthbar,(10,10))
    for health1 in range(health_value):
        screen.blit(health,(health1+13,13))

    #7 - update the screen
    pygame.display.flip()    
    
    #8- processing   All events in a queue
    for event in pygame.event.get():        
        #quit
        if  event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
            
        #keyboard_press 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                keys[0]=True
            elif event.key == pygame.K_a:
                keys[1]=True
            elif event.key == pygame.K_s:
                keys[2]=True
            elif event.key == pygame.K_d:
                keys[3]=True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                keys[0]=False
            elif event.key == pygame.K_a:
                keys[1]=False
            elif event.key == pygame.K_s:
                keys[2]=False
            elif event.key == pygame.K_d:
                keys[3]=False

        #mouse_press
        if event.type == pygame.MOUSEBUTTONDOWN:
            shoot.play()
            position=pygame.mouse.get_pos()
            acc[1]+=1
            arrows.append([math.atan2(postion[1]-(player_pos[1]+32),postion[0]-(player_pos[0]+32)),player_pos1[0]+32,player_pos1[1]+32])

    #player_move
    if keys[0]:
        player_pos[1]-=4
    elif keys[2]:
        player_pos[1]+=4
    if keys[1]:
        player_pos[0]-=4
    elif keys[3]:
        player_pos[0]+=4

    #10 win or lose
    if pygame.time.get_ticks() >= 60000:
        running=0
        exitcode=1
    if health_value <= 0:
        running=0
        exitcode=0
    if acc[1] != 0:
        accuracy=acc[0]*1.0/acc[1]*100
    else:
        accuracy=0
    #print accuracy

#11 win or lose display
if exitcode == 0:
    pygame.font.init()
    font=pygame.font.Font(None,24)
    text=font.render("Accuracy: "+str(accuracy)[:5]+"%",True,(255,0,0))
    textRect=text.get_rect()
    textRect.centerx=screen.get_rect().centerx
    textRect.centery=screen.get_rect().centery+24
    screen.blit(gameover,(0,0))
    screen.blit(text,textRect)
else:
    pygame.font.init()
    font=pygame.font.Font(None,24)
    text=font.render("Accuracy: "+str(accuracy)[:5]+"%",True,(255,0,0))
    textRect=text.get_rect()
    textRect.centerx=screen.get_rect().centerx
    textRect.centery=screen.get_rect().centery+24
    screen.blit(youwin,(0,0))
    screen.blit(text,textRect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        pygame.display.flip()


