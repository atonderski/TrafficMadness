import math
import sys

import pygame

from traffic_madness.drawer import Drawer


class PyGameDrawer(Drawer):
    def __init__(self, resolution, title, track):
        pygame.init()
        self.track = track
        self.screen, self.bg_surface = self.setup_screen(resolution, title)

        # Clock used to for update
        self.clock = pygame.time.Clock()
        self.fps = 10

        # Car constants for painting
        self.CAR_COLOR = pygame.Color(175, 70, 2, 255)
        self.CAR_SIZE = 10

        self.LANE_WIDTH = round(float(resolution[0]) / self.track.track_length)
        self.LANE_HEIGHT = resolution[1] / 2.

        # Paint the screen
        self.screen.blit(self.bg_surface, (0, 0))
        pygame.display.flip()

    def setup_screen(self, resolution, title):
        """ Set up and return screen and background."""
        screen = pygame.display.set_mode(resolution)
        pygame.display.set_caption(title)

        bg_surface = pygame.Surface(screen.get_size())
        bg_surface = bg_surface.convert()
        BG_COLOR = pygame.Color(255, 255, 255, 255)
        bg_surface.fill(BG_COLOR)
        return screen, bg_surface

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.display.quit()
                    pygame.quit()
                    sys.exit()

    def update(self, cars):
        self.event_loop()

        def _rect_from_car(car):
            r = 350 + 20 * (self.track.num_lanes - car.lane)
            theta = -car.position * 2*math.pi / self.track.track_length
            x = 500 + r * math.cos(theta)
            y = 500 + r * math.sin(theta)
            return pygame.Rect(x, y, self.CAR_SIZE, self.CAR_SIZE)

        car_rects = [_rect_from_car(car) for car in cars]

        self.screen.blit(self.bg_surface, (0, 0))

        for index, car_rect in enumerate(car_rects):
            print(car_rect)
            rect_surface = pygame.Surface(car_rect.size)
            rect_surface.fill(self.CAR_COLOR)
            self.screen.blit(rect_surface, (car_rect.x, car_rect.y))
        print("Number of cars: " + str(len(car_rects)))
        pygame.display.flip()
        self.clock.tick(self.fps)
