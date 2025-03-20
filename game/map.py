# import sys, pygame
# from PyQt5.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QGraphicsRectItem
# from PyQt5.QtGui import QBrush, QColor
# from PyQt5.QtCore import Qt

# FPS = 60
# WIDTH, HEIGHT = 800, 600
# TILE_SIZE = 40  # 타일 크기

# clock = pygame.time.Clock()
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.init()

# class GameView(QGraphicsView):
#     def __init__(self):
#         super().__init__()

#         # 씬(Scene) 생성
#         self.scene = QGraphicsScene()
#         self.setScene(self.scene)
#         self.setFixedSize(WIDTH, HEIGHT)
        
#         # 맵 레이아웃 (0: 빈 공간, 1: 벽, 2: 불, 3: 물, 4: 늪, 5: 도착지)
#         self.map_data = [
#             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 1],
#             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#             [1, 4, 4, 1, 1, 1, 1, 3, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1],
#             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
            
#         ]

#         self.walls = []
#         self.tiles = []
#         self.draw_map()

#         # # fireboy
#         # self.fireboy = QGraphicsRectItem(60,60,TILE_SIZE, TILE_SIZE)
#         # self.fireboy.setBrush(QBrush(Qt.red))
#         # self.scene.addItem(self.fireboy)

#         # # watergirl
#         # self.watergirl = QGraphicsRectItem(100, 60, TILE_SIZE, TILE_SIZE)
#         # self.watergirl.setBrush(QBrush(Qt.blue))
#         # self.scene.addItem(self.watergirl)

#     def draw_map(self):
#         """맵을 그리는 함수"""
#         for row_index, row in enumerate(self.map_data):
#             for col_index, tile in enumerate(row):
#                 x, y = col_index * TILE_SIZE, row_index * TILE_SIZE
                
#                 # 벽 (회색)
#                 if tile == 1:
#                     block = QGraphicsRectItem(x, y, TILE_SIZE, TILE_SIZE)
#                     block.setBrush(QBrush(Qt.gray))
#                     self.scene.addItem(block)
#                     self.walls.append(block) 
                
#                 # 불 웅덩이 (빨간색)
#                 elif tile == 2:
#                     fire = QGraphicsRectItem(x, y, TILE_SIZE, TILE_SIZE/2)
#                     fire.setBrush(QBrush(Qt.red))
#                     self.scene.addItem(fire)
#                     self.tiles.append(fire)
                
#                 # 물 웅덩이 (파란색)
#                 elif tile == 3:
#                     water = QGraphicsRectItem(x, y, TILE_SIZE, TILE_SIZE/2)
#                     water.setBrush(QBrush(Qt.blue))
#                     self.scene.addItem(water)
#                     self.tiles.append(water)
                    
#                 # 늪 (검은색)
#                 elif tile == 4 :
#                     swamp = QGraphicsRectItem(x, y, TILE_SIZE, TILE_SIZE/2)
#                     swamp.setBrush(QBrush(Qt.black))
#                     self.scene.addItem(swamp)
#                     self.tiles.append(swamp)

#                 # 도착지 빛 (노란색)
#                 elif tile == 5 :
#                     dest = QGraphicsRectItem(x, y, TILE_SIZE/2, TILE_SIZE/2)
#                     dest.setBrush(QBrush(Qt.yellow))
#                     self.scene.addItem(dest)
#                     self.tiles.append(dest)
    
#     def check_collision(self, player):
#         player_rect = pygame.Rect(player.x, player.y, TILE_SIZE, TILE_SIZE)
        
#         for tile in self.tiles:
#             tile_rect = tile.sceneBoundingRect()
#             if player_rect.colliderect(tile_rect):
#                 return tile    
#         return None
    
#     # def keyPressEvent(self, event):
#     #     key = event.key()
#     #     move_amount = 10

#     #     if key == Qt.Key_Right:
#     #         self.move_character(self.fireboy, move_amount, 0)
#     #     elif key ==Qt.Key_Left:
#     #         self.move_character(self.fireboy, -move_amount, 0)

#     #     if key == Qt.Key_D:
#     #         self.move_character(self.watergirl, move_amount, 0)
#     #     elif key ==Qt.Key_A:
#     #         self.move_character(self.watergirl, -move_amount, 0)

#     # def move_character(self, chracter, dx, dy):
#     #     new_x = chracter.x() +dx
#     #     new_y = chracter.y() +dy

#     #     for wall in self.walls:
#     #         if wall.sceneBoundingRect().contains(new_x, new_y):
#     #             return
            
#     #     chracter.moveBy(dx, dy)
    

# class Player():
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#         self.velocity = 10
#         self.isJump = False
        
#     def draw(self):
#         return pygame.draw.rect(screen, (0,255,0), (self.x, self.y, 40, 40))
    
#     def jump(self):
#         if self.isJump:
#             if self.velocity >= -10:
#                 neg =1
#                 if self.velocity < 0:
#                     neg =-1
#                 self.y -= self.velocity **2 * 0.7 * neg
#                 self.velocity -= 1
#             else:
#                 self.isJump = False
#                 self.velocity = 10
    
#     def move_fire(self):
#         if pressedKeys[K_RIGHT]:
#             self.x += 5
        
#     def move_water(self):
#         if pressedKeys[K_d]:
#             self.x += 5
# player_fire = Player(40, HEIGHT-40)
# player_water = Player(50, HEIGHT-40)
            

# def main():
#     app = QApplication(sys.argv)
#     view = GameView()
#     view.show()
#     sys.exit(app.exec_())

#     while(True):
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
        
#         clock.tick(FPS)
#         screen.fill((255,255,255))
        
#         global pressedKeys
#         pressedKeys = pygame.key.get_pressed()
        
#         player_water_rect = player_water.draw()
#         player_water.move()
#         player_water.jump()
        
#         player_fire_rect = player_fire.draw()
#         player_fire.move()
#         player_fire.jump()
        
#         collision_tile1 = view.check_collision(player_fire)
#         if collision_tile1:
#             if collision_tile == view.tiles[3]:
#                 print("물 터치")
#             elif collision_tile == view.tiles[4]:
#                 print("늪 오버")
            
#         collision_tile2 = view.check_collision(player_water)
#         if collision_tile2:
#             if collision_tile == view.tiles[2]:
#                 print("불 터치")
#             elif collision_tile == view.tiles[4]:
#                 print("늪 오버")
                
#         if collision_tile1 and collision_tile2:
#             if collision_tile1 == view.tiles[5]:
#                 if collision_tile2 == view.tiles[5]:
#                     print("게임 성공")
#                     break


# if __name__ == "__main__":
#     main()

import sys
import pygame

# 게임 설정
FPS = 60
WIDTH, HEIGHT = 800, 600
TILE_SIZE = 40  # 타일 크기

# 색상 정의
COLOR_GRAY = (169, 169, 169)
COLOR_RED = (255, 0, 0)
COLOR_BLUE = (0, 0, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_YELLOW = (255, 255, 0)

# pygame 초기화
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# 맵 레이아웃 (0: 빈 공간, 1: 벽, 2: 불, 3: 물, 4: 늪, 5: 도착지)
map_data = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 4, 4, 1, 1, 1, 1, 3, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]



# 플레이어 클래스
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocity = 10

    def update(self, keys):
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.velocity
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.velocity
        if keys[pygame.K_DOWN]:
            self.rect.y += self.velocity
        if keys[pygame.K_UP]:
            self.rect.y -= self.velocity

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

# 맵 그리기 함수
# def draw_map():
#     for row_index, row in enumerate(map_data):
#         for col_index, tile in enumerate(row):
#             x, y = col_index * TILE_SIZE, row_index * TILE_SIZE
#             if tile == 1:
#                 pygame.draw.rect(screen, COLOR_GRAY, (x, y, TILE_SIZE, TILE_SIZE))
#             elif tile == 2:
#                 pygame.draw.rect(screen, COLOR_RED, (x, y, TILE_SIZE, TILE_SIZE // 2))
#             elif tile == 3:
#                 pygame.draw.rect(screen, COLOR_BLUE, (x, y, TILE_SIZE, TILE_SIZE // 2))
#             elif tile == 4:
#                 pygame.draw.rect(screen, COLOR_BLACK, (x, y, TILE_SIZE, TILE_SIZE // 2))
#             elif tile == 5:
#                 pygame.draw.rect(screen, COLOR_YELLOW, (x, y, TILE_SIZE // 2, TILE_SIZE // 2))

walls = []
tiles = []
                
def draw_map(self):
        for row_index, row in enumerate(self.map_data):
            for col_index, tile in enumerate(row):
                x, y = col_index * TILE_SIZE, row_index * TILE_SIZE
                
                # 벽 (회색)
                if tile == 1:
                    pygame.draw.rect(screen, COLOR_GRAY, (x, y, TILE_SIZE, TILE_SIZE))
                    self.scene.addItem(block)
                    walls.append(block) 
                
                # 불 웅덩이 (빨간색)
                elif tile == 2:
                    pygame.draw.rect(screen, COLOR_RED, (x, y, TILE_SIZE, TILE_SIZE // 2))
                    self.scene.addItem(fire)
                    tiles.append(fire)
                
                # 물 웅덩이 (파란색)
                elif tile == 3:
                    pygame.draw.rect(screen, COLOR_BLUE, (x, y, TILE_SIZE, TILE_SIZE // 2))
                    self.scene.addItem(water)
                    tiles.append(water)
                    
                # 늪 (검은색)
                elif tile == 4 :
                    pygame.draw.rect(screen, COLOR_BLACK, (x, y, TILE_SIZE, TILE_SIZE // 2))
                    self.scene.addItem(swamp)
                    tiles.append(swamp)

                # 도착지 빛 (노란색)
                elif tile == 5 :
                    pygame.draw.rect(screen, COLOR_YELLOW, (x, y, TILE_SIZE // 2, TILE_SIZE // 2))
                    self.scene.addItem(dest)
                    tiles.append(dest)


# 충돌 체크 함수
def check_collision(player, tile_list):
    for tile in tile_list:
        if player.rect.colliderect(tile.rect):
            return tile
    return None

def main():
    # 게임 객체 생성
    fireboy = Player(40, HEIGHT - 2*TILE_SIZE, COLOR_RED)
    watergirl = Player(80, HEIGHT - 2*TILE_SIZE, COLOR_BLUE)

    all_sprites = pygame.sprite.Group()
    all_sprites.add(fireboy)
    all_sprites.add(watergirl)

    # 게임 루프
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 키 입력 받기
        keys = pygame.key.get_pressed()
        
        # 게임 화면 업데이트
        screen.fill((255, 255, 255))  # 배경색
        draw_map()  # 맵 그리기
        all_sprites.update(keys)  # 플레이어 위치 업데이트
        all_sprites.draw(screen)  # 화면에 플레이어 그리기

        # 충돌 체크
        collision_tile1 = check_collision(fireboy, all_sprites)
        collision_tile2 = check_collision(watergirl, all_sprites)

        # 충돌 처리 (예: 물에 터치하면 "불 터치" 출력)
        if collision_tile1:
            if isinstance(collision_tile1, Player):
                print("불 터치")
        if collision_tile2:
            if isinstance(collision_tile2, Player):
                print("물 터치")

        pygame.display.flip()  # 화면 업데이트
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
