# Don't forget source venv/bin/activate to init virtual environment innit
import sys
import os
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot



def main():
    pygame.init()
    pygame.font.init()

    score = 0
    score_increment = 10
    font = pygame.font.Font('hobo.ttf', 36)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()



    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updatable:
            obj.update(dt)

        screen.fill("black")

        score_text = font.render(f'Score: {score}', True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        for asteroid in asteroids:
            if asteroid.collision_check(player):  # game over stuffs
                screen.fill("black")
                death_text = font.render(f"Game Over! Final Score: {score}", True, (255, 255, 255))
                screen.blit(death_text, (SCREEN_WIDTH / 2 - death_text.get_width() / 2, SCREEN_HEIGHT / 3))
                exit_text = font.render("Press any key to exit", True, (255, 255, 255))
                screen.blit(exit_text, (SCREEN_WIDTH / 2 - exit_text.get_width() / 2, SCREEN_HEIGHT / 2))
                
                pygame.display.flip()

                waiting_for_key = True
                while waiting_for_key:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            return
                        elif event.type == pygame.KEYDOWN:  # any key press to exit
                            waiting_for_key = False
                            pygame.quit()
                            sys.exit()

            for shot in shots:
                if asteroid.collision_check(shot):
                    shot.kill()
                    asteroid.split()
                    score += score_increment

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
