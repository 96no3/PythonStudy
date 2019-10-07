import pygame
from pygame.locals import *
import sys

def main():
    (w,h) = (400, 400)   # 画面サイズ
    (x,y) = (200, 200)   # プレイヤー画像の初期位置（画面中央）
    pygame.init()       # pygame初期化
    pygame.display.set_mode((w, h), 0, 32)  # 画面設定
    screen = pygame.display.get_surface()
    
    # 背景画像（bg.jpg）の取得
    bg = pygame.image.load("C:\\texture\\bg.png").convert_alpha()    
    rect_bg = bg.get_rect()

    # プレイヤー画像(player.png)の取得
    player = pygame.image.load("C:\\texture\\player.png").convert_alpha()    
    rect_player = player.get_rect()
    rect_player.center = (x, y) # プレイヤー画像の初期位置

    while (1):
        # キーイベント処理(キャラクタ画像の移動)
        pressed_key = pygame.key.get_pressed()
        # 「←」キーが押されたらx座標を-5に移動
        if pressed_key[K_LEFT]:
            rect_player.move_ip(-5, 0)
        # 「→」キーが押されたらx座標を+5移動
        if pressed_key[K_RIGHT]:
            rect_player.move_ip(5, 0)
        # 「↑」キーが押されたらy座標を-5移動
        if pressed_key[K_UP]:
            rect_player.move_ip(0, -5)
        # 「↓」キーが押されたらy座標を+5移動
        if pressed_key[K_DOWN]:
            rect_player.move_ip(0, 5)
        
        pygame.display.update()             # 画面更新
        pygame.time.wait(30)                # 更新時間間隔
        screen.fill((0, 20, 0, 0))          # 画面の背景色
        screen.blit(bg, rect_bg)            # 背景画像の描画
        screen.blit(player, rect_player)    # プレイヤー画像の描画

        # 終了用のイベント処理
        for event in pygame.event.get():
            # 閉じるボタンが押されたとき
            if event.type == QUIT:          
                pygame.quit()
                sys.exit()

            # キーを押したとき
            if event.type == KEYDOWN:       
                if event.key == K_ESCAPE:   # Escキーが押されたとき
                    pygame.quit()
                    sys.exit()

if __name__ == "__main__":
        main()
