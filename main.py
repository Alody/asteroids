# Don't forget source venv/bin/activate to enter venv
import pygame
import os
os.environ['SDL_AUDIODRIVER'] = 'dsp'
from constants import *

def main():
    pygame.init()
    clock = pygame.time.Clock() # instantiate clock
    dt = 0 # delta time
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    while True:
        for event in pygame.event.get(): # loop until user quits
            if event.type == pygame.QUIT:
                return 
        screen.fill("black") # fill with black
        pygame.display.flip() # update display
        dt = clock.tick(60) / 1000 # framerate to 60 fps and return amount of time since last call (delta time)


if __name__ == "__main__":
    main()