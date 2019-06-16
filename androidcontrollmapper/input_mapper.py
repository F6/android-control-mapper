from loguru import logger

logger.disable('pyminitouch')

# import configs
from profile_PUBG import *

# ----------------- pygame init -----------------

import pygame

pygame.init()

# Set the width and height of the screen [width,height]
WHITE = (255,255,255)
size = [500, 500]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Controller Status")

# enter virtual input mode of mouse
pygame.mouse.set_visible(False)
pygame.event.set_grab(True)

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# ----------------- end pygame init -----------------

# -------- Main Program Loop -----------


# Loop until the user clicks the close button.
done = False
while done == False:

    # EVENT PROCESSING STEP
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                done = True
            elif event.key in BUTTON_KEY_BINDING:
                # deal with buttons
                # print("triggering push", event.key)
                BUTTON_KEY_BINDING[event.key].activate()
            elif event.key in JOYSTICK_KEY_BINDING:
                # joysticks deactivate themselves when all controll keys are released,
                # so no need to deactivate them at here.
                JOYSTICK_KEY_BINDING[event.key].activate()

        elif event.type == pygame.KEYUP:
            if event.key in BUTTON_KEY_BINDING:
                BUTTON_KEY_BINDING[event.key].deactivate()

        elif event.type == pygame.MOUSEMOTION:
            fpsmouse.activate()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button in BUTTON_MOUSE_BUTTON_BINDING:
                BUTTON_MOUSE_BUTTON_BINDING[event.button].activate()

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button in BUTTON_MOUSE_BUTTON_BINDING:
                BUTTON_MOUSE_BUTTON_BINDING[event.button].deactivate()

    screen.fill(WHITE)

    # update widgets, if any
    for widget in updating_widgets_list:
        if widget.activated == True:
            widget.update()

    # commit all changes
    tem.update()

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()

device.stop()
