import pygame
from constants import *
from player import Player

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
    player1 = Player(x,y)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
           
        screen.fill("black")
        player1.draw(screen)
        pygame.display.flip()
        ms=FPS.tick(60)
        dt = ms / 1000

        
        
    
    


if __name__ == "__main__":
    main()
