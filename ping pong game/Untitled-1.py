from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x,size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < width - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < width - 80:
            self.rect.y += self.speed 


back = (200, 255, 255)
width = 600
height = 500
window = display.set_mode((width,height))
game = True
Finsih = False
clock = time.Clock()
FPS = 60
speed_x = 3
speed_y = 3
Platform_left = Player("racket.png",30,250,40,100,15)
Platform_right = Player("racket.png",520,250,40,100,15)
ball = GameSprite("tenis_ball.png",200,200,50,50,20)
font.init()
font1 = font.Font(None, 36)
player1win = font1.render("PLAYER 1 win!", True,(190,0,0))
player2win = font1.render("PLAYER 2 win!", True,(190,0,0))
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not Finsih:
        window.fill(back)
        Platform_left.reset()
        Platform_right.reset()
        ball.reset()
        Platform_left.update_l()
        Platform_right.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_x



    if ball.rect.y > height-50 or ball.rect.y < 0 :
        speed_y *= -1

    if sprite.collide_rect(Platform_left,ball)or sprite.collide_rect(Platform_right,ball):
        speed_x *= -1
        speed_y *= 1

    if ball.rect.x > width:
        Finish = True
        window.blit(player1win,(200,200))

    if ball.rect.x < 0:
        Finish = True
        window.blit(player2win,(200,200))



    display.update()
    clock.tick(FPS)