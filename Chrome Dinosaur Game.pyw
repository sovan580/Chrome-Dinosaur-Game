import pygame
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((600,500))
pygame.display.set_caption("Chrome Dino Game")
font=pygame.font.Font('freesansbold.ttf',20)
font1=pygame.font.Font('freesansbold.ttf',35)
font2=pygame.font.Font('freesansbold.ttf',15)
white=(255,255,255)
tree=pygame.image.load("tree.png")
tree=pygame.transform.scale(tree,(70,50))
tree1=pygame.image.load("tree1.png")
tree1=pygame.transform.scale(tree1,(100,60))
tree2=pygame.image.load("tree2.png")
tree2=pygame.transform.scale(tree2,(90,60))
tree3=pygame.image.load("tree3.png")
tree3=pygame.transform.scale(tree3,(45,60))
tree4=pygame.image.load("tree4.png")
tree4=pygame.transform.scale(tree4,(70,60))
dino1=pygame.image.load("dra1.png")
dino1=pygame.transform.scale(dino1,(50,50))
dino2=pygame.image.load("dra2.png")
dino2=pygame.transform.scale(dino2,(50,50))
dino3=pygame.image.load("dra3.png")
dino3=pygame.transform.scale(dino3,(50,50))
dino4=pygame.image.load("dra4.png")
dino4=pygame.transform.scale(dino4,(50,50))
dino5=pygame.image.load("dra5.png")
dino5=pygame.transform.scale(dino5,(50,50))
background=pygame.image.load("background.png")
walk=[dino1,dino1,dino1,dino1,dino2,dino2,dino2,dino2,dino3,dino3,dino3,dino3,dino4,dino4,dino4,dino4]

def gameloop():
    back_x=0
    back_y=0
    bac_x_vel=0
    tree_x=650
    tree_y=282
    dino_x=50
    dino_y=275
    gravity=4
    walkpoint=0
    run=False
    jump=False
    score=0
    gameOver=False
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
            if event.type==KEYDOWN:
                if event.key==K_SPACE:
                    if dino_y==275:
                        jump=True
                        bac_x_vel=3
                        run=True
                if event.key==K_RETURN:
                    gameloop()
                  
        if back_x==-600:
            back_x=0
        if tree_x<-1600:
            tree_x=550
        if 276>dino_y>125:
            if jump==True:
                dino_y-=4
        else:
            jump=False
        if dino_y<275:
            if jump==False:
                dino_y+=gravity
        if tree_x< dino_x + 50 < tree_x + 70 and tree_y<dino_y+50<tree_y+50:
            bac_x_vel=0
            walkpoint=0
            run=False
            gameOver=True
        if tree_x+400< dino_x + 50 < tree_x + 470 and tree_y<dino_y+50<tree_y+50:
            bac_x_vel=0
            walkpoint=0
            run=False
            gameOver=True
        if tree_x+800< dino_x + 50 < tree_x + 870 and tree_y<dino_y+50<tree_y+50:
            screen.blit(dino5,(dino_x,dino_y))
            bac_x_vel=0
            walkpoint=0
            run=False
            gameOver=True
        if tree_x+1200< dino_x + 50 < tree_x + 1270 and tree_y<dino_y+50<tree_y+50:
            bac_x_vel=0
            walkpoint=0
            run=False
            gameOver=True
        if tree_x+1600< dino_x + 50 < tree_x + 1670 and tree_y<dino_y+50<tree_y+50:
            bac_x_vel=0
            walkpoint=0
            run=False
            gameOver=True

        if run==True:
            score+=1
        
        screen.fill(white)
        text=font.render("Score : "+str(score), True,(0,0,0))
        text1=font1.render("GAME OVER",True,(0,0,0))
        text2=font2.render("Press Enter To Continue",True,(0,0,0))
        back_x-=bac_x_vel
        tree_x-=bac_x_vel
        screen.blit(background,(back_x,back_y))
        screen.blit(background,(back_x+600,back_y))
        screen.blit(text,(360,50))
        if gameOver==True:
            screen.blit(text1,(200,120))
            screen.blit(text2,(220,170))
        screen.blit(walk[walkpoint],(dino_x,dino_y))
        if run==True:
            walkpoint+=1
            if walkpoint>15:
                walkpoint=0
        screen.blit(tree,(tree_x,tree_y))
        screen.blit(tree1,(tree_x+400,tree_y))
        screen.blit(tree2,(tree_x+800,tree_y-8))
        screen.blit(tree3,(tree_x+1200,tree_y-8))
        screen.blit(tree4,(tree_x+1600,tree_y-2))
        pygame.display.update()
gameloop()
pygame.quit()
quit()

