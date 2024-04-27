from pygame import*

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x,player_y,sise_x,sise_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(sise_x,sise_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
       window.blit(self.image,(self.rect.x,self.rect.y)) 

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed 
        if keys_pressed[K_RIGHT] and self.rect.x < win_height - 80:
            self.rect.x += self.speed 
    def fire(self):
        bullet = Bullet('bullet.png',self.rect.centerx,self.rect.top,15,20,15)
        bullets.add(bullet) 









