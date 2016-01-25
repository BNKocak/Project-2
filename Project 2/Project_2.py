import time
from threading import Thread
import os, pygame
import time
import random
from Node import *
from Players import *
pygame.init()
size = width, height = 1700, 1080
black = 0, 0, 0
white = 255, 255, 255
green = 50, 255, 100
screen = pygame.display.set_mode(size)
offset = 50
size = 10


#---------------------------------------------------------------------------
board = pygame.image.load("Content/Board.jpg")
menu = pygame.image.load("Content/Menu.jpg") 
play = pygame.image.load("Content/Play.png").convert_alpha()
play_hover = pygame.image.load("Content/Play_hover.png").convert_alpha()
exit = pygame.image.load("Content/Quit.png").convert_alpha()
exit_hover = pygame.image.load("Content/Quit_hover.png").convert_alpha()
number2 = pygame.image.load("Content/#1.png").convert_alpha()
number3 = pygame.image.load("Content/#2.png").convert_alpha()
number4 = pygame.image.load("Content/#3.png").convert_alpha()
number2_hover = pygame.image.load("Content/#1_hover.png").convert_alpha()
number3_hover = pygame.image.load("Content/#2_hover.png").convert_alpha()
number4_hover = pygame.image.load("Content/#3_hover.png").convert_alpha()
dice_1 = pygame.image.load("Content/1.png").convert_alpha()
dice_2 = pygame.image.load("Content/2.png").convert_alpha()
dice_3 = pygame.image.load("Content/3.png").convert_alpha()
dice_4 = pygame.image.load("Content/4.png").convert_alpha()
dice_5 = pygame.image.load("Content/5.png").convert_alpha()
dice_6 = pygame.image.load("Content/6.png").convert_alpha()
dice = pygame.image.load("Content/dice.png").convert_alpha()
pion = pygame.image.load("Content/pion.png").convert_alpha()

number2_r = play.get_rect()
number2_r.x, number2_r.y = (705, 360)
number3_r = play.get_rect()
number3_r.x, number3_r.y = (705, 460)
number4_r = play.get_rect()
number4_r.x, number4_r.y = (705, 560)

play_r = play.get_rect()
play_r.x, play_r.y = (705, 360)
exit_r = exit.get_rect()
exit_r.x, exit_r.y = (705, 460)
dice_r = dice.get_rect()
dice_r.x, dice_r.y = (1180, 300)
dicelist = [dice_1, dice_2, dice_3, dice_4, dice_5, dice_6]
#----------------------------------------------------------------------------


def Main():
  start = time.time()
  playing = False
  currentscreen = 0
  Hover_play_r = False
  Hover_exit_r = False
  diceclicked = False
  Hover_number2_r = False
  Hover_number3_r = False
  Hover_number4_r = False
  TilePlayerBlue = Node(Position(33, 33), Node(Position(140, 33), Node(Position(140, 33), Node(Position(220, 33), Node(Position(300, 33), Node(Position(380, 44), Node(Position(505, 33), Node(Position(625, 33),\
        Node(Position(705, 33), Node(Position(785, 33), Node(Position(865, 33), Node(Position(975, 33), Empty))))))))))))
  FirstPlayer = Player1(TilePlayerBlue, pion)

  while True:    
    pygame.event.pump() 
    # 0 = First Menu
    # 1 = After menu > amount players
    # 2 = Board game
    # 3 = Pause menu
    if playing == False and currentscreen == 0:                     # HOVER OVER BUTTONS
        if Hover_play_r == True:
            screen.blit(play_hover, (705,360))
            currentscreen = 0
        elif Hover_exit_r == True:
            screen.blit(exit_hover, (705, 460))
            currentscreen = 0
        else:
            #screen.fill(black)
            screen.blit(menu, (0,0))
            screen.blit(play, (705,360))
            screen.blit(exit, (705,460))
            currentscreen = 0
    if playing == True and currentscreen == 1:
        if Hover_number2_r == True:
            screen.blit(number2_hover, (705, 360))
            currentscreen = 1
        elif Hover_number3_r == True:
            screen.blit(number3_hover, (705, 460))
            currentscreen = 1
        elif Hover_number4_r == True:
            screen.blit(number4_hover, (705, 560))
            currentscreen = 1
        else:
            screen.blit(number2, (705,360))
            screen.blit(number3, (705,460))
            screen.blit(number4, (705,560))
            currentscreen = 1
        
    for event in pygame.event.get():                                # for loop EVENT iteration
        if play_r.collidepoint(pygame.mouse.get_pos()):             # HOVER CHECK
            Hover_play_r = True
        else:
            Hover_play_r = False
        if exit_r.collidepoint(pygame.mouse.get_pos()):
            Hover_exit_r = True
        else:
            Hover_exit_r = False
        if number2_r.collidepoint(pygame.mouse.get_pos()):
            Hover_number2_r = True
        else:
            Hover_number2_r = False
        if number3_r.collidepoint(pygame.mouse.get_pos()):
            Hover_number3_r = True
        else:
            Hover_number3_r = False
        if number4_r.collidepoint(pygame.mouse.get_pos()):
            Hover_number4_r = True
        else:
            Hover_number4_r = False
        
        if event.type == pygame.MOUSEBUTTONUP:                      # EVEN PROCESSING MOUSECLICKS
            pos = pygame.mouse.get_pos()
            pos_x = pos[0]
            pos_y = pos[1]
            print(pos_x)
            print(pos_y)
            if (pos_x > 704) and (pos_x < 960) and (pos_y > 359) and (pos_y < 406) and currentscreen == 0:
                print("PLAY")
                playing = True
                if playing == True and currentscreen == 0:
                    screen.fill(black)
                    pygame.font.init()
                    myfont = pygame.font.SysFont("calibri", 50)
                    label = myfont.render("Choose amount of players", 1, (0, 0, 0))
                    screen.blit(menu, (0,0))
                    screen.blit(label, (560, 120))
                    screen.blit(number2, (705,360))
                    screen.blit(number3, (705,460))
                    screen.blit(number4, (705,560))
                    currentscreen = 1
            elif (pos_x > 704) and (pos_x < 960) and (pos_y > 459) and (pos_y < 506) and currentscreen == 0:
                print("QUIT")
                pygame.quit()
            elif (pos_x > 704) and (pos_x < 961) and (pos_y > 359) and (pos_y < 403):
                if currentscreen == 1:
                    currentscreen = 2
            elif (pos_x > 704) and (pos_x < 961) and (pos_y > 359) and (pos_y < 503):
                if currentscreen == 1:
                    currentscreen = 2
            elif (pos_x > 704) and (pos_x < 961) and (pos_y > 359) and (pos_y < 603):
                if currentscreen == 1:
                    currentscreen = 2
            elif dice_r.collidepoint(pygame.mouse.get_pos()):
                i = random.randint(0, 5)
                screen.blit(dicelist[i], (1180, 300))
                diceclicked = True
                playing = True

        if event.type == pygame.KEYDOWN:                                                # PAUSE SCREEN
            if event.key == pygame.K_ESCAPE:
                playing = False
                screen.fill(black)
                screen.blit(play, (705,360))
                screen.blit(exit, (705,460))
                currentscreen = 3
    if currentscreen == 2:                                                              # Playing Board Screen
        if diceclicked == False:
            screen.fill(black)
            screen.blit(board, (0,0))
            screen.blit(pion, (FirstPlayer.MyTile.Value.PositionX,FirstPlayer.MyTile.Value.PositionX))
            screen.blit(pion, (FirstPlayer.MyTile.Tail.Value.PositionX,FirstPlayer.MyTile.Tail.Value.PositionY))
            screen.blit(pion, (220,33))
            screen.blit(pion, (300,33))
            screen.blit(pion, (380,33))
            screen.blit(pion, (505,33))
            screen.blit(pion, (625,33))
            screen.blit(pion, (705,33))
            screen.blit(pion, (785,33))
            screen.blit(pion, (865,33))
            screen.blit(pion, (975,33))
            screen.blit(dice, (1180, 300))
        if event.type == pygame.MOUSEMOTION:
            print("mouse at (%d, %d)" % event.pos)
    
    pygame.display.flip()
    time.sleep(0.01)
    
Main()