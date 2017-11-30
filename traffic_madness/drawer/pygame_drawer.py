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
        self.fps = 60

        self.background_surface = pygame.Surface(self.screen.get_size())
        self.background_surface = self.background_surface.convert()
        BG_COLOR = pygame.Color(255, 255, 255, 255)
        self.background_surface.fill(BG_COLOR)

        self.CAR_COLOR = (175, 70, 2, 255)
        self.screen.blit(self.background_surface, (0, 0))

        self.rect_size = 2

        pygame.display.flip()

    def update(self, cars):
        car_rects = [pygame.Rect(car.position,
                                 200 + 50 * car.lane,
                                 self.rect_size,
                                 self.rect_size)
                     for car in cars]

        self.screen.blit(self.background_surface, (0, 0))

        for index, car_rect in enumerate(car_rects):
            print(car_rect)
            rect_surface = pygame.Surface(car_rect.size)
            rect_surface.fill(self.CAR_COLOR)
            self.screen.blit(rect_surface, (car_rect.x, car_rect.y))
        print("Number of cars: " + str(len(car_rects)))
        pygame.display.flip()
        self.clock.tick(self.fps)
