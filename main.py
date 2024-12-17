# Don't forget source venv/bin/activate to enter venv
import pygame
import os
os.environ['SDL_AUDIODRIVER'] = 'dsp'
from constants import *
from player import Player


def main():
    pygame.init()
    clock = pygame.time.Clock() # instantiate clock
    dt = 0 # delta time
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    updatable = pygame.sprite.Group() # group of updatable (position) sprites
    drawable = pygame.sprite.Group() # group of drawable sprites

    Player.containers = (updatable, drawable) # put Player class in both groups

    while True:
        for event in pygame.event.get(): # loop until user quits
            if event.type == pygame.QUIT:
                return 
            
        for i in updatable:
            i.update(dt)

        screen.fill("black") # fill with black

        for i in drawable:
            i.draw(screen)

        pygame.display.flip() # update display
        dt = clock.tick(60) / 1000 # framerate to 60 fps 


if __name__ == "__main__":
    main()