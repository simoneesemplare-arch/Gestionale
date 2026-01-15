import pygame
from components import map
from components.map import TileKind, Map
from components.sprite import Sprite, sprites 
def main():
# pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    tile_kinds = [
        TileKind("grass", "Gestionale/Tiny Swords (Update 010)/Terrain/Ground/Tilemap_Flat_Small.PNG"),
        TileKind("yellow", "Gestionale/Tiny Swords (Update 010)/Terrain/Ground/Tilemap_FlatYellow_Small.PNG"),
        ]
    map=Map("Gestionale/src/components/maps/start.map", tile_kinds, 53)
    Sprite("Gestionale/Tiny Swords (Update 010)/Deco/18.png", 5*25, 5*14)
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("dark green")
        
        # RENDER YOUR GAME HERE
        map.draw(screen)
        for s in sprites:
            s.draw_sprites(screen)
        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()


if __name__ == "__main__":
    main()
