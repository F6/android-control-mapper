from loguru import logger
import pygame
from pyminitouch import MNTDevice
import time

from touch_event_manager import TouchEventManager
import widgets

from _DEVICE_ID import _DEVICE_ID
device = MNTDevice(_DEVICE_ID)

tem = TouchEventManager(device)

operation_start_button_1 = widgets.Button(
    tem,
    name='operation_start_1',
    center=(985, 2160 - 1938)
)

operation_start_button_2 = widgets.Button(
    tem,
    name='operation_start_2',
    center=(763, 2160 - 1772)
)

give_up_operation_button = widgets.Button(
    tem,
    name='give_up_operation',
    center=(763, 2160 - 775)
)

# -------- Main Program Loop -----------

# do this for 180 times ( 180 * 15 = 2700 )
try:
    for i in range(18):
        logger.info("No: {i}".format(i=i))

        # touch the start button, get into character selection
        logger.info("Selecting Level")
        logger.info("Waiting for loading, 20 seconds")

        for j in range(20):
            operation_start_button_1.activate()
            tem.update()
            time.sleep(0.5)
            operation_start_button_1.deactivate()
            tem.update()
            time.sleep(0.5)

        # touch the operation start button, start the stage
        logger.info("Start Operation")
        operation_start_button_2.activate()
        tem.update()
        time.sleep(0.5)
        operation_start_button_2.deactivate()
        tem.update()

        # wait for stage finish
        logger.info("Waiting for operation finish")
        for j in range(11):
            time.sleep(10.0)
            logger.info("waited for {j}0.0 seconds".format(j=j+1))

        # touch anywhere to return to level selection
        logger.info(
            "Returning to level selection, if PRTS messed up, then give up operation")
        give_up_operation_button.activate()
        tem.update()
        time.sleep(0.5)
        give_up_operation_button.deactivate()
        tem.update()
        time.sleep(0.5)
        # just touch the same place as level selection, so go into next loop

except KeyboardInterrupt:
    logger.info("Keyboard Interrupt Received, Exiting Gracefully")
    device.stop()
