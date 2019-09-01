from abc import ABC, abstractmethod
import pygame


class GameWidget(ABC):
    '''
    Game Widgets are those controllable elements in a game. For example, 
    buttons, switches, and on-screen joysticks.

    All Widgets are controlled by the InputMapper.

    3 methods must be implemented: activate, deactivate, and update.

    After a widget is activated, the update method will be called once per frame,
    until it is deactivated.
    '''

    def __init__(self, touch_event_manager, name='unnamed widget', activated=False):
        self.touch_event_manager = touch_event_manager
        self.name = name
        self.activated = False
        self.touch_id = -1

    @abstractmethod
    def activate(self):
        pass

    @abstractmethod
    def deactivate(self):
        pass

    @abstractmethod
    def update(self):
        pass


class Button(GameWidget):
    '''
    those widgets on screen that can be touched.
    radius is optional, it is only required when randomizing touch positions is needed.
    '''

    def __init__(self, touch_event_manager, name='unnamed button', activated=False, center=(0, 0), radius=0):
        self.center = center
        self.radius = radius
        super().__init__(touch_event_manager, name=name, activated=activated)

    def activate(self):
        if self.activated == True:
            return
        self.touch_id = self.touch_event_manager.get_touch_id(self)
        # print('down', self, self.touch_id, self.center)
        # SAFE GUARD
        self.touch_event_manager.command_builder.commit()
        self.touch_event_manager.command_builder.down(
            self.touch_id,
            *self.center, 50)
        self.activated = True

    def deactivate(self):
        if self.activated == False:
            return
        # print('up', self)
        # SAFE GUARD
        self.touch_event_manager.command_builder.commit()
        self.touch_event_manager.command_builder.up(self.touch_id)
        self.touch_event_manager.reclaim_touch_id(self)
        self.touch_id = -1
        self.activated = False

    def update(self):
        pass


class Joystick(GameWidget):
    '''
    those widgets on screen that emulates a real joystick, 
    commonly used in mobile games to controll moving.
    '''

    def __init__(self, touch_event_manager, name='unnamed joystick',
                 activated=False, center=(0, 0), radius=0,
                 flip_axis=False, flip_x=False, flip_y=False):
        self.center = center
        self.radius = radius
        self.flip_axis = flip_axis
        self.flip_x = flip_x
        self.flip_y = flip_y
        self.last_coordinates = None
        super().__init__(touch_event_manager, name=name, activated=activated)

    def activate(self):
        if self.activated == True:
            return
        self.touch_id = self.touch_event_manager.get_touch_id(self)
        # print('down', self, self.touch_id, self.center)
        # SAFE GUARD
        self.touch_event_manager.command_builder.commit()
        self.touch_event_manager.command_builder.down(
            self.touch_id,
            *self.center, 50)
        self.activated = True

    def deactivate(self):
        if self.activated == False:
            return
        # SAFE GUARD: empty commit before up
        self.touch_event_manager.command_builder.commit()
        self.touch_event_manager.command_builder.up(self.touch_id)
        self.touch_event_manager.reclaim_touch_id(self)
        self.touch_id = -1
        self.last_coordinates = None
        self.activated = False

    def update(self):
        input_axis = self.get_keyboard_input_axis(
            flip_axis=self.flip_axis, flip_x=self.flip_x, flip_y=self.flip_y)
        # deactivates itself if no control key is pressed
        if input_axis == (0.0, 0.0):
            # Notice that this critiria is only valid for keyboard input.
            # If the user uses joystick input, a small dead zone is needed
            # since the joysticks in general do not go back to zero point
            # when released.
            self.deactivate()
            return
        new_coordinates = (int(self.center[0] + input_axis[0] * self.radius),
                           int(self.center[1] + input_axis[1] * self.radius))
        if new_coordinates == self.last_coordinates:
            # if nothing is changed, then the command can be safely omitted.
            pass
        else:
            # SAFE GUARD: empty commit before move
            self.touch_event_manager.command_builder.commit()
            self.touch_event_manager.command_builder.move(
                self.touch_id,
                *new_coordinates, 50)
        self.last_coordinates = new_coordinates

    @staticmethod
    def get_keyboard_input_axis(flip_axis=False, flip_x=False, flip_y=False):
        # this is only for keyboard. For joystick input, just use pygame's
        # Joystick.get_axis()
        x = 0.0
        y = 0.0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            x -= 1.0000001
        if keys[pygame.K_s]:
            x += 1.0
        if keys[pygame.K_a]:
            y -= 1.0000001
        if keys[pygame.K_d]:
            y += 1.0

        if flip_x:
            x = -x
        if flip_y:
            y = -y

        if flip_axis:
            return (x, y)
        else:
            return (y, x)


class FPSMouse(GameWidget):
    '''
    FPSMouse drags the screen when mouse 
    is moved, commonly used in FPS mobile games to controll aiming
    '''

    def __init__(self, touch_event_manager,
                 name='unnamed fpsmouse', activated=False, center=(0, 0),
                 sensitivity=1,
                 flip_axis=False, flip_x=False, flip_y=False):
        self.center = center
        self.sensitivity = sensitivity
        self.flip_axis = flip_axis
        self.flip_x = flip_x
        self.flip_y = flip_y
        self.last_coordinates = None
        super().__init__(touch_event_manager, name=name, activated=activated)

    def activate(self):
        if self.activated == True:
            return
        self.touch_id = self.touch_event_manager.get_touch_id(self)
        # SAFE GUARD
        self.touch_event_manager.command_builder.commit()
        self.touch_event_manager.command_builder.down(
            self.touch_id,
            *self.center, 50)
        # initial point of cumulative motion
        self.last_coordinates = self.center
        self.activated = True

    def deactivate(self):
        if self.activated == False:
            return
        # SAFE GUARD: empty commit before up
        self.touch_event_manager.command_builder.commit()
        self.touch_event_manager.command_builder.up(self.touch_id)
        self.touch_event_manager.reclaim_touch_id(self)
        self.touch_id = -1
        self.last_coordinates = None
        self.activated = False

    def update(self):
        mouse_delta = self.get_mouse_delta(
            flip_axis=self.flip_axis, flip_x=self.flip_x, flip_y=self.flip_y)
        # print(mouse_delta)
        # deactivates itself if mouse_delta is zero
        if mouse_delta == (0, 0):
            # Notice that this critiria is only valid for mouse input.
            # If the user uses joystick input, a small dead zone is needed
            # since the joysticks in general do not go back to zero point
            # when released.
            self.deactivate()
            return
        new_coordinates = (int(self.last_coordinates[0] + mouse_delta[0] * self.sensitivity),
                           int(self.last_coordinates[1] + mouse_delta[1] * self.sensitivity))

        # SAFE GUARD: empty commit before move
        self.touch_event_manager.command_builder.commit()
        self.touch_event_manager.command_builder.move(
            self.touch_id,
            *new_coordinates, 50)
        self.last_coordinates = new_coordinates

    @staticmethod
    def get_mouse_delta(flip_axis=False, flip_x=False, flip_y=False):
        # this is only for mouse. For joystick input, just use pygame's
        # Joystick.get_axis()

        mouse_delta = pygame.mouse.get_rel()
        x = mouse_delta[0]
        y = mouse_delta[1]

        if flip_x:
            x = -x
        if flip_y:
            y = -y

        if flip_axis:
            return (x, y)
        else:
            return (y, x)
