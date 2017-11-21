import pygame
from traffic_madness.drawer import Drawer


class PyGameDrawer(Drawer):

    def __init__(self, resolution, title, track):
        pygame.init()
        self.track = track
        
        SCREEN_RESOLUTION = resolution
        self.screen = pygame.display.set_mode(resolution)
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()

        self.background_surface = pygame.Surface(screen.get_size())
        self.background_surface = backgroun_surface.convert()
        BG_COLOR = pygame.color(255,255,255,255)
        self.background_surface.fill(BG_COLOR)

        self.screen.blit(background_surface, (0, 0))

        self.rect_size = 5

        pygame.display.flip()

    def update(car_positions):
        car_rects = [pygame.Rect(pos, 350, self.rect_size, self.rect_size)
                     for pos in car_positions]
        rect_surfaces = [pygame.Surface(rect.size)
                         for rect in car_rects]
        
        
