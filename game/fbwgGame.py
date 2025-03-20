# 파란 사각형과, 빨간 사각형
# 맵 내에 블루존, 레드존 설치
# 지형을 통해 최종 목적지에 도착하면 성공
# 동일한 색이 아닌 존에 닿으면 게임오버
import pygame
from pygame.locals import *
import os
from PyQt5.QtWidgets import *
from PyQt5 import uic
import time
import sys
from PyQt5.QtCore import Qt, QTimer

class Game(QMainWindow):
    def __init__(self):
        super().__init__()
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        uic.loadUi("map.ui", self)

        self.fireboy = self.


# 배경 맵 깔기
os.chdir(os.path.dirname(os.path.abspath(__file__)))
ui_path = "map.ui"
form_class = uic.loadUiType(ui_path)[0] 

#세팅
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Fireboy and Watergirl (Mini Version)")

WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
BLACK = (0,0,0)

clock = pygame.time.Clock()
FPS =60

running = True

# 플레이어 
fireboy = pygame.Rect(100, 500, 40, 40)
watergirl = pygame.Rect(200,500,40,40)

# 장애물 추가
lava = pygame.Rect(200,300,100,20)
water = pygame.Rect(300,500,100,20)

def check_collision():
    if fireboy.colliderect(water):
        print("fireboy 게임오버")
        return True
    if watergirl.colliderect(lava):
        print("watergirl 게임오버")
        return True
    return False

def jump(self, pygame.rect.Rect):
    gravity = 10
    pygame.rect.Rect.y -= gravity
    time.sleep(0.2)
    pygame.rect.Rect.y += gravity

# 메인 함수
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    keys = pygame.key.get_pressed()
    speed = 5
    if keys[pygame.K_LEFT]:
        fireboy.x -= speed
    if keys[pygame.K_RIGHT]:
        fireboy.x += speed
    if keys[pygame.K_UP]:
        fireboy.jump()
    if keys[pygame.K_DOWN]:
        fireboy.y += speed
        
    if keys[pygame.K_a]:
        watergirl.x -= speed
    if keys[pygame.K_d]:
        watergirl.x += speed
    if keys[pygame.K_w]:
        watergirl.y -= speed
    if keys[pygame.K_s]:
        watergirl.y += speed

    # 장애물, 웅덩이 그리기
    pygame.draw.rect(screen, RED, fireboy)
    pygame.draw.rect(screen, BLUE, watergirl)
    pygame.draw.rect(screen, RED, lava) #(255,100,100)
    pygame.draw.rect(screen, BLUE, water) #V

    if check_collision():
        running = False

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()

    
    
        
    

# global red_zone, blue_Zone
# touched = False

# class Player:
#     def __init__(self,color):
#         self.color = color

#     def draw(self):
#         return pygame.draw.rect()        
    
#     def move(self):
#         # 3개 방향키 (위가 점프)
        
#     def isTouched(self):
#         if (redPlayer == blue_zone or bluePlyaer == red_zone ):
#             touched = True


    
# class Obstacle:
#     def __init__():
#         # 1단계 맵은 고정되어있으니까 그냥 세팅만 주면 된다
#     def draw():


# bluePlyaer = Player(blue)
# redPlayer = Player(red)
# map1 = Obstacle()


# if '__name__' == '__main__':
#     main

