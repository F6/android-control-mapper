import pygame
from pyminitouch import MNTDevice
import time

from touch_event_manager import TouchEventManager
import widgets

from _DEVICE_ID import _DEVICE_ID
device = MNTDevice(_DEVICE_ID)

tem = TouchEventManager(device)

################ Define Widgets ################

# Buttons

reload_button = widgets.Button(
    tem, 
    name='reload', 
    center=(1080 - 1005, 1701)
    )

jump_button = widgets.Button(
    tem,
    name='jump',
    center=(1080 - 754, 2075)
)

crouch_button = widgets.Button(
    tem,
    name='crouch',
    center=(1080 - 1012, 1852)
)

get_down_button = widgets.Button(
    tem,
    name='get_down',
    center=(1080 - 954, 2054)
)

weapon_1_button = widgets.Button(
    tem,
    name='weapon_1',
    center=(1080 - 1012, 2160 // 2 - 200)
)

weapon_2_button = widgets.Button(
    tem,
    name='weapon_2',
    center=(1080 - 1012, 2160 // 2 + 200)
)

weapon_3_button = widgets.Button(
    tem,
    name='weapon_3',
    center=(1080 - 1000, 1430)
)

lean_left_button = widgets.Button(
    tem,
    name='lean_left',
    center=(1080 - 400, 275)
)

lean_right_button = widgets.Button(
    tem,
    name='lean_right',
    center=(1080 - 400, 425)
)

pick_up_first_item_button = widgets.Button(
    tem,
    name='pick_up_first_item',
    center=(1080 - 390 ,1500)
)

pick_up_second_item_button = widgets.Button(
    tem,
    name='pick_up_second_item',
    center=(1080 - 490 ,1500)
)

fire_button = widgets.Button(
    tem,
    name='fire',
    center=(1080 - 812, 1865)
)

aim_button = widgets.Button(
    tem,
    name='aim',
    center=(1080 - 568, 2088)
)

open_box_button = widgets.Button(
    tem,
    name='open_box',
    center=(1080 - 300, 1500)
)

get_out_car_button = widgets.Button(
    tem,
    name='get_out_car_button',
    center=(1080 - 380, 1960)
)

# Joysticks

move_joystick = widgets.Joystick(
    tem,
    name='move',
    center=(270, 344),
    radius=300,
    flip_axis=True, flip_x=True
)

# FPSMouses

fpsmouse = widgets.FPSMouse(
    tem,
    name='fpsmouse',
    center=(1080 // 2, 2160 // 2 + 50),
    sensitivity=0.5,
    flip_y=True
)

################ End Define Widgets ################


################ Define Bindings ################

BUTTON_KEY_BINDING = {
    pygame.K_r:     reload_button,
    pygame.K_SPACE: jump_button,
    pygame.K_c:     crouch_button,
    pygame.K_v:     get_down_button,
    pygame.K_1:     weapon_1_button,
    pygame.K_2:     weapon_2_button,
    pygame.K_3:     weapon_3_button,
    pygame.K_q:     lean_left_button,
    pygame.K_e:     lean_right_button,
    pygame.K_f:     pick_up_first_item_button,
    pygame.K_g:     pick_up_second_item_button,
    pygame.K_z:     open_box_button,
    pygame.K_b:     get_out_car_button,
}

BUTTON_MOUSE_BUTTON_BINDING = {
    1:              fire_button,
    3:              aim_button,
}

JOYSTICK_KEY_BINDING = {
    pygame.K_w:     move_joystick,
    pygame.K_s:     move_joystick,
    pygame.K_a:     move_joystick,
    pygame.K_d:     move_joystick,
}

################ End Define Bindings ################

updating_widgets_list = [move_joystick, fpsmouse]