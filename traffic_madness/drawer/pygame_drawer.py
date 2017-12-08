import math
import sys

import pygame

from traffic_madness.drawer import Drawer
from traffic_madness.config import Config


class PyGameDrawer(Drawer):
    def __init__(self, resolution, title, track):
        pygame.init()
        self.track = track
        self.screen, self.bg_surface = self.setup_screen(resolution, title)

        # Clock used to for update
        self.clock = pygame.time.Clock()
        self.fps = 10

        # Car constants for painting
        # self.CAR_COLOR = pygame.Color(175, 70, 2, 255)
        self.CAR_SIZE = 10

        self.LANE_WIDTH = round(float(resolution[0]) / self.track.track_length)
        self.LANE_HEIGHT = resolution[1] / 2.

        # Paint the screen
        self.screen.blit(self.bg_surface, (0, 0))
        pygame.display.flip()

        # Add a font to write stuff
        self.font = pygame.font.SysFont('Arial', 20)

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

    def update(self, cars, time, flow):
        config = Config()
        self.event_loop()

        def _rect_from_car(car):
            r = 350 + 20 * (self.track.num_lanes - car.lane)
            theta = -car.position * 2 * math.pi / self.track.track_length
            x = 500 + r * math.cos(theta)
            y = 500 + r * math.sin(theta)
            return pygame.Rect(x - self.CAR_SIZE/2,
                               y - self.CAR_SIZE/2,
                               self.CAR_SIZE,
                               self.CAR_SIZE)

        car_rects = [_rect_from_car(car) for car in cars]

        self.screen.blit(self.bg_surface, (0, 0))

        ''' Beginning changes in drawer T.F.'''
        # Add rectangle with text into the middle of the circle
        rect = pygame.Rect(400, 480, 200, 40)
        pygame.draw.rect(self.bg_surface, (0, 0, 0), rect, 2)
        flow_text = 'Traffic flow: {:.4f} cars/h'.format(flow)
        self.screen.blit(self.font.render(flow_text, True, (0, 0, 0)), (405, 487))
        # Add number of cars to drawer to indicate state of initialisation
        cars_text = '# Cars: {:d}'.format(len(cars))
        self.screen.blit(self.font.render(cars_text, True, (0, 0, 0)), (450, 520))
        # Add current time to drawer
        time_text = 'Time: {:.2f} s'.format(time * config.timestep)
        self.screen.blit(self.font.render(time_text, True, (0, 0, 0)), (450, 540))

        ''' End changes in drawer T.F.'''

        for index, car_rect in enumerate(car_rects):
            rect_surface = pygame.Surface(car_rect.size)
            rect_surface.fill(cars[index].color)
            self.screen.blit(rect_surface, (car_rect.x, car_rect.y))


        # circles
        for i in range(1,self.track.num_lanes+2):
            pygame.draw.circle(self.screen, pygame.Color(0, 0, 0), (500, 500),
                               (340 + 20 * i), 1)

        pygame.display.flip()
        self.clock.tick(self.fps)
