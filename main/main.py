import pygame
from pathlib import Path

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

running = True
fps = 120
clock = pygame.time.Clock()

while running:
    # 從pygame事件佇列中，一項一項的檢查
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()  # 更新螢幕狀態
    dt = clock.tick(fps)

pygame.quit()  # 關閉繪圖視窗
