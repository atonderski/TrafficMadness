import pygame
from random import randint

def main():
    # Initialize the pygame modules
    pygame.init()
    # Constant for size of created screen window
    SCREEN_RESOLUTION = (720, 720)
    # Create a screen window with a set size
    screen = pygame.display.set_mode(SCREEN_RESOLUTION)
    # Set title
    pygame.display.set_caption("Pygame example")
    # Clock object to control time/ticks
    clock = pygame.time.Clock()

    # Create a background surface,  same size as our screen window
    background_surface = pygame.Surface(screen.get_size())
    # Convert background surface to single pixel format, not really
    # important when we only have one object. Good practice
    background_surface = background_surface.convert()
    BG_COLOR = pygame.Color(255,255,255,255) # RGBAm white
    background_surface.fill(BG_COLOR) # Paint surface with color
    # Blit the background surface onto the screen with upper left in (0,0).
    # This fills the entire screen since our bg is the same size as screen
    screen.blit(background_surface, (0, 0))

    # Initial values for rectangle object.
    x_pos = 500 # Starting x pixel from upper left
    y_pos = 500 # Starting y pixel from upper left
    x_vel = -1 # Move in x, yes
    y_vel = 0 # Move in y, no
    color = pygame.Color(175, 70, 2, 255) #RGBA, some orange.
    speed = 1 # Number of pixels moved each iteration.
    size = 40 # Number of pixels width/height

    # Create our rectangle object, no color, just pos and size
    rect = pygame.Rect(x_pos, y_pos, size, size)
    # Create our rectangle surface, with size of our rect object
    rect_surface = pygame.Surface(rect.size)
    # Convert to single pixel format, again not that important here
    rect_surface.convert()
    # Fill the surface with our color
    rect_surface.fill(color)
    # Blit the rectangle surface(with color) to the screen at position of our rect object
    screen.blit(rect_surface, (rect.x, rect.y))
    
    # This updates the whole screen, 
    # pygame.display.update() equivalent, but update() can also
    # update only specific parts of screen. See loop below
    pygame.display.flip()
   # Main event and draw loop
    running = True
    while running:

        # Loop through the events pygame get
        for event in pygame.event.get():
            # Pressed the exit button
            if event.type == pygame.QUIT:
                running = False
            # Pressed down a button
            if event.type == pygame.KEYDOWN:
                # Space key, boost
                if event.key == pygame.K_SPACE:
                    speed = boost(speed)
                # Arrow key presses
                # Up
                elif event.key == pygame.K_UP:
                   x_vel = 0
                   y_vel = -1
                # Down
                elif event.key == pygame.K_DOWN:
                    x_vel = 0
                    y_vel = 1
                # Left
                elif event.key == pygame.K_LEFT:
                    x_vel = -1
                    y_vel = 0
                # Right
                elif event.key == pygame.K_RIGHT:
                    x_vel = 1
                    y_vel = 0
            # On click of mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                #Get mouse positions
                x, y = pygame.mouse.get_pos()
                # Check if we clicked inside our rectangle object
                if rect.collidepoint(x,y):
                    # Set a random color on our rectangle surface
                    color = pygame.Color(randint(0,255),
                                         randint(0,255),
                                         randint(0,255),
                                         255)
                    rect_surface.fill(color)

        # We don't want to repaint the whole screen every loop. Only surfaces of
        # objects that have changed (dirty). This is done by blitting a subsurface of 
        # the backgroundsurface onto the screen in the position of the
        # rectangle object (matching where the rectangle surface was painted)
        
        # Get clean background at position of dirty subsurface
        dirty_rect_subsurface = background_surface.subsurface(rect)
        #Get a copy of the dirty rect object for updating later
        dirty_rect = rect.copy()
        # Blit the clean background subsurface to the screen at rect pos
        # to clean the dirty rectangle
        screen.blit(dirty_rect_subsurface, (rect.x, rect.y))
        
        # Now the screen is only white background. We painted over our rect
        # Want to paint it again at an updates position.

        # Update our rect objects position
        update_rect(rect, x_vel, y_vel, speed, SCREEN_RESOLUTION)
        # Then blit the rectangle surface to the screen at the new
        # position of the rectangle object
        screen.blit(rect_surface, (rect.x, rect.y))
        
        # If we have more than one rect, we don't do this for every rect but
        # only check those who moved in maybe a list of dirty rects

        # Needed to update our screen, only update the parts that have changed
        # Update the rectangle surface at position of rectangle
        pygame.display.update(rect)
        # Update the dirty surface we painted over above
        pygame.display.update(dirty_rect)
        
        # More effective if many, do a list of rects to update such as 
        # rect_list = [rect, dirty_rect_subsurface]
        # pygame.display.update(rect_list)


        #pygame.display.flip() to update whole screen, maybe if transition to 
        #new background.

        # ~60 fps
        clock.tick(60)

def update_rect(rect, x_vel, y_vel, speed, resolution):
    rect.x += x_vel*speed
    rect.y += y_vel*speed
    #Check if we are outside bounds.
    # Don't use constant here, se
    if rect.x > resolution[0] - 1 - rect.width:
        rect.x = resolution[0] - 1 - rect.width
    if rect.x < 0:
        rect.x = 0
    if rect.y > resolution[1] - 1 - rect.height:
        rect.y = resolution[1] - 1 - rect.height
    if rect.y < 0:
        rect.y = 0

def boost(speed):
    return speed*2

if __name__ == '__main__':
    main()

