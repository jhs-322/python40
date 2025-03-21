import pygame, sys

FPS = 60
MAX_WIDTH = 600
MAX_HEIGHT = 400   

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))

class Player():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.isJump = False
        self.jumpCount = 10
    def draw(self):
        return pygame.draw.rect(screen, (0,0,255), (self.x, self.y, 40, 40))
    def jump(self):
        if self.isJump:
            if self.jumpCount >= -10: # -10보다 큰데
                neg = 1
                if self.jumpCount < 0: # 음수일 때
                    neg = -1 # jumpCount랑 곱했을 때 양수로 만들어줘야 하니까
                self.y -= self.jumpCount**2 * 0.7 * neg 
                self.jumpCount -= 1
                
            else: # -10보다 작을 때 = 점프 10번 하면
                self.isJump = False
                self.jumpCount = 10
                
player = Player(MAX_WIDTH/2, MAX_HEIGHT-40) #자신의 높이 = 40

def main():
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.isJump = True
        
        clock.tick(FPS)
        screen.fill((255,255,255))
        
        player_rect = player.draw()
        player.jump()
        
        print(player_rect)
        pygame.display.update()
        
if __name__ == "__main__":
    main()