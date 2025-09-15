import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    FPS=pygame.time.Clock()
    dt=0
    x=SCREEN_WIDTH/2
    y=SCREEN_HEIGHT/2
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable,drawable)
    player1 = Player(x,y)
    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = (updatable,)
    asfield = AsteroidField()
    Shot.containers = (shots,drawable,updatable)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
           
        screen.fill("black")
        updatable.update(dt)
        for asteroid in asteroids:
            if player1.collision(asteroid):
                print ("Game over!")
                raise SystemExit 
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collision(shot):
                    asteroid.split()
                    pygame.sprite.Sprite.kill(shot)
        for item in drawable:
            item.draw(screen) 
        pygame.display.flip()
        ms=FPS.tick(60)
        dt = ms / 1000

        
        
    
    


if __name__ == "__main__":
    main()
