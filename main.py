import pygame
from constants import *
from circleshape import CircleShape
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

    drawables = pygame.sprite.Group()
    updatables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (drawables, updatables)
    Asteroid.containers = (asteroids, drawables, updatables)
    AsteroidField.containers = (updatables)
    Shot.containers = (drawables, updatables, shots)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    clock = pygame.time.Clock()
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatables.update(dt)
        for asteroid in asteroids:
            if asteroid.isColliding(player):
                print("Game Over!")
                exit(0)
            for shot in shots:
                if asteroid.isColliding(shot):
                    asteroid.split()
                    shot.kill()

        screen.fill((0,0,0))
        for drawable in drawables:
            drawable.draw(screen)


        pygame.display.flip()
        dt = clock.tick(120.0) / 1000





if __name__ == "__main__":
    main()