import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    # initialization
    clock = pygame.time.Clock();
    dt = 0; # deltaTime

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # create groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    # initialize sprites after grouping
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidField = AsteroidField()

    # update loop
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
    
        for obj in drawable:
            obj.draw(screen)
        
        for obj in updatable:
            obj.update(dt)
        
        pygame.display.flip() # updates display

        for asteroid in asteroids:
            if asteroid.is_colliding(player):
                print("Game over!")
                exit(0)
            
            for shot in shots:
                if shot.is_colliding(asteroid):
                    pygame.sprite.Sprite.kill(shot)
                    pygame.sprite.Sprite.kill(asteroid)
                    break

        dt = clock.tick(60) / 1000 # delay game loop for 1/60th of a second, and also calculate time since last frame


if __name__ == "__main__":
    main()