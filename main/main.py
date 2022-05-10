import pygame
from pathlib import Path
from player import Player
from missile import MyMissile

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

# 建立物件串列
Missiles = []


keyCountX = 0  # 用來計算按鍵被按下的次數，X軸
keyCountY = 0

# 建立事件編號
launchMissile = pygame.USEREVENT + 1


running = True
clock = pygame.time.Clock()  # create an object to help track time

while running:
    # 從pygame事件佇列中，一項一項的檢查
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == launchMissile:
            m_x = player.xy[0] - 10
            m_y = player.xy[1]
            Missiles.append(MyMissile(xy=(m_x, m_y), playground=playground, sensitivity=movingScale))
            m_x = player.xy[0] + 40
            Missiles.append(MyMissile(xy=(m_x, m_y), playground=playground, sensitivity=movingScale))

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:  # 'a', 'A', 左移
                keyCountX += 1
                player.to_the_left()
            if event.key == pygame.K_d:
                keyCountX += 1
                player.to_the_right()
            if event.key == pygame.K_s:
                keyCountY += 1
                player.to_the_bottom()
            if event.key == pygame.K_w:
                keyCountY += 1
                player.to_the_top()

            if event.key == pygame.K_SPACE:
                m_x = player.x - 10
                m_y = player.y
                Missiles.append(MyMissile(xy=(m_x, m_y), playground=playground, sensitivity=movingScale))
                m_x = player.x + 40
                Missiles.append(MyMissile(playground, (m_x, m_y), movingScale))  # 若未指定參數，須按照宣告順序
                pygame.time.set_timer(launchMissile, 200)  # 之後，每400 ms發射一組

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                if keyCountX == 1:
                    keyCountX = 0
                    player.stop_x()
                else:
                    keyCountX -= 1
            if event.key == pygame.K_s or event.key == pygame.K_w:
                if keyCountY == 1:
                    keyCountY = 0
                    player.stop_y()
                else:
                    keyCountY -= 1

            if event.key == pygame.K_SPACE:
                pygame.time.set_timer(launchMissile, 0)  # 停止發射

    screen.blit(background, (0, 0))  # 更新背景圖片

    Missiles = [item for item in Missiles if item.available]
    for m in Missiles:
        m.update()
        screen.blit(m.image, m.xy)

    player.update()  # 更新player狀態
    screen.blit(player.image, player.xy)  # 添加 player 圖片
    pygame.display.update()  # 更新螢幕狀態
    dt = clock.tick(fps)  # 每秒更新 fps 次

pygame.quit()  # 關閉繪圖視窗
