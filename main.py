import pygame
from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player


def main():
    print(f"Starting Asteroids with pygame verson {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init() 
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
    clock = pygame.time.Clock()
    dt = 0.0 # delta time in seconds

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    # Add all future instances of player to updatable and drawable groups
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        log_state()

        # Close game on window's X button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Do stuff on the screen before updating
        screen.fill("black")
        
        # Update rotaion based on dt
        updatable.update(dt) 

        # Draw objects in drawable group
        for d in drawable:
            d.draw(screen)

        # Update the contents of the display
        pygame.display.flip()
        
        # Cap at 60 fps
        dt = clock.tick(60) / 1_000


if __name__ == "__main__":
    main()
