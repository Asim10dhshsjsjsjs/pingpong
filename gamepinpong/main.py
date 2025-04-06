from pygame import * 
from random import *

window = display.set_mode((700, 500)) 
display.set_caption("pinpong") 
background = transform.scale(image.load("fon.png"),(700,500))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_x, size_y))    
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player (GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.y >= 6:
            self.rect.y -= self.speed
        if keys[K_d] and self.rect.y <= 420:
            self.rect.y += self.speed


class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()

class Enemy(GameSprite):
  def update_r(self):
        keys = key.get_pressed()
        if keys[K_RIGHT] and self.rect.y >= 6:
            self.rect.y -= self.speed
        if keys[K_LEFT] and self.rect.y <= 420:
            self.rect.y += self.speed
      

player = Player("racket.png",10,390,20,75,5)
enemy = Enemy("racket.png",660,390,20,75,5)
finish=False            
game = True

while game: 
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
    
        window.blit(background,(0,0))
#       if sprite.groupcollide(bullets, enemys, True, True):
#          score += 1
        player.update_l()
        player.reset()
        enemy.reset()
        enemy.update_r()
        display.update()

    time.delay(8)