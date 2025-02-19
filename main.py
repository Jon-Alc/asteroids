import pygame
from constants import *
from player import Player

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
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

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
        dt = clock.tick(60) / 1000 # delay game loop for 1/60th of a second, and also calculate time since last frame


if __name__ == "__main__":
    main()