import pygame
from pathlib import Path
from player import Player

# 初始化pygame系統
pygame.init()

# 設定視窗物件，寬、高
screenHigh = 760
screenWidth = 1000
playground = [screenWidth, screenHigh]
screen = pygame.display.set_mode((screenWidth, screenHigh))

parent_path = Path(__file__).parents[1]
print(parent_path)
image_path = parent_path / 'res'
print(image_path)
icon_path = image_path / 'airplaneicon.png'
print(icon_path)

# Title, Icon, and Background
pygame.display.set_caption('1942偽')
icon = pygame.image.load(icon_path)  # 載入圖示
pygame.display.set_icon(icon)
background = pygame.Surface(screen.get_size())
background.fill((50, 50, 50))  # 畫布圍鐵黑色(三個參數為RGB)
background = background.convert()  # 改變pixel format，加快顯示速度

fps = 120  # 更新頻率，包含畫面更新與事件更新
movingScale = 600 / fps  # 大約 600 pixel / second

player = Player(playground=playground, sensitivity=movingScale)

running = True
clock = pygame.time.Clock()  # create an object to help track time

while running:
    # 從pygame事件佇列中，一項一項的檢查
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:  # 'a', 'A', 左移
                player.to_the_left()
            if event.key == pygame.K_d:
                player.to_the_right()
            if event.key == pygame.K_s:
                player.to_the_bottom()
            if event.key == pygame.K_w:
                player.to_the_top()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                player.stop_x()
            if event.key == pygame.K_s or event.key == pygame.K_w:
                player.stop_y()

    screen.blit(background, (0, 0))  # 更新背景圖片
    player.update()  # 更新player狀態
    screen.blit(player.image, player.xy)  # 添加 player 圖片
    pygame.display.update()  # 更新螢幕狀態
    dt = clock.tick(fps)  # 每秒更新 fps 次

pygame.quit()  # 關閉繪圖視窗
