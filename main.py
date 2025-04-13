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



class Enemy(GameSprite):
  def update_r(self):
        keys = key.get_pressed()
        if keys[K_RIGHT] and self.rect.y >= 6:
            self.rect.y -= self.speed
        if keys[K_LEFT] and self.rect.y <= 420:
            self.rect.y += self.speed
      

player = Player("racket.png",10,390,20,75,15)
enemy = Enemy("racket.png",660,390,20,75,15)
ball = GameSprite("tenis_ball.png",50,390,40,35,5)
score = 0
finish=False            
game = True
font.init()
font1 = font.SysFont('Arial', 36)

text_lose = font1.render(
    "player 1 lost:",True,(255,0,0)
)
text_lose2 = font1.render(
    "player 2 lost:",True,(255,0,0)
)
text_vin1 = font1.render("отбито:" + str(score),1, (255,255,255))

speed_x = 6
speed_y = 6

while game:
    
    window.blit(background,(0,0))
    text_vin1 = font1.render("отбито:" + str(score),1, (255,255,255))
    window.blit(text_vin1, (10,20)) 
    for e in event.get():

        if e.type == QUIT:
            game = False
    if not finish:

        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > 460 or ball.rect.y < 3:
            speed_y *= -1
        if sprite.collide_rect(player, ball) or sprite.collide_rect(enemy, ball):
            speed_x *= -1
            score +=1
        if ball.rect.x < 3:
            window.blit(text_lose,(350,250))
            finish = True
        if ball.rect.x > 640:
            window.blit(text_lose2,(350,250))
            finish = True
        
        
        ball.update()
        ball.reset()
        player.update_l()
        player.reset()
        enemy.reset()
        enemy.update_r()

        display.update()

    time.delay(25)