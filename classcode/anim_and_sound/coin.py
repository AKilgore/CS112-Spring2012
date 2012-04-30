from random import randrange

from pygame import Surface
from pygame.sprite import Sprite, Group
from anim import Anmation, AnimationFrames
from spritesheet import Spritesheet

COIN_FRAMES = None
COIN_SPRITES = None

class CoinAnimation(Animation):
    duration = 25

    def __init__(self):
        global COIN_FRAMES, COIN_SPRITES

        if COIN_FRAMES is None:
            COIN_FRAMES = AnimationFrames([
                    (self.duration, (0,0)),
                    (self.duration, (1,0)),
                    (self.duration, (2,0)),
                    (self.duration, (3,0)),
                    (self.duration, (4,0)),
                    (self.duration, (5,0)),
                    (self.duration, (6,0)),
                    (self.duration, (7,0))
                    ])
        if COIN_SPRITES is None:
            COIN_SPRITES = SpriteSheet("coin", (8,1))
        
        Animation.__init__(self, COIN_SPRITES, COIN_FRAMES)

## Coin
class Coin(Sprite):
    def __init__(self, loc):
        Sprite.__init__(self)

        self.image = self.create_image()
        self.rect = self.image.get_rect()
        self.rect.center = loc

    def create_image(self):
        image = Surface((15, 15))
        rect = image.get_rect()
        image.fill((0,0,0), rect)
        image.fill((255,255,0), rect.inflate(-2,-2))
        return image

    def update(self, dt):
        pass

class CoinGroup(Group):
    spawn_rate = 1000   # ms

    def __init__(self, bounds):
        Group.__init__(self)

        self.bounds = bounds
        self.spawn_timer = 0

    def spawn(self):
        x = randrange(self.bounds.x, self.bounds.x + self.bounds.width)
        y = randrange(self.bounds.y, self.bounds.y + self.bounds.height)

        coin = Coin((x,y))
        coin.rect.clamp_ip(self.bounds)
        self.add(coin)

    def update(self, dt):
        Group.update(self, dt)
    
        # update the spawner
        self.spawn_timer += dt
        if self.spawn_timer >= self.spawn_rate:
            self.spawn()
            self.spawn_timer = 0

