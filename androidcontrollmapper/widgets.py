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

