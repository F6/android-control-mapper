from pyminitouch import CommandBuilder
from loguru import logger

class TouchEventManager():
    '''
    Manages all touch events in each frame for a single device.

    At each frame, a new CommandBuilder is prepared for all widgets.
    '''

    def __init__(self, device):
        self.device = device
        self.touch_id_max = 10
        self.widget_touch_id = dict()
        self.command_builder = CommandBuilder()

    # touch id methods

    def get_touch_id(self, widget):
        '''
        assigns a touch id to a widget
        '''
        assigned_ids = self.widget_touch_id.values()
        for i in range(self.touch_id_max):
            if i not in assigned_ids:
                self.widget_touch_id[widget] = i
                return i
        logger.error("Cannot assign new touch id to widget {widget_name}".format(
            widget_name=widget.name))

    def reclaim_touch_id(self, widget):
        '''
        reclaim the touch id previously assigned to a widget
        '''
        if self.widget_touch_id[widget] != -1:
            self.widget_touch_id[widget] = -1
            return
        logger.error("Already reclaimed touch id of widget {widget_name}".format(
            widget_name=widget.name))

    # button methods

    def update(self):
        '''
        All actions are delayed until update of TouchEventManager is called, 
        so that in a single
        frame no contradictory actions are performed (for example, touching and
        releasing a button at the same frame should not be allowed because it is 
        not physically possible.)
        this method of TouchEventManager should be called only after all 
        widgets updates are called.
        '''

        # commit all changes
        # if nothing is to be done in this frame, don't send anything.
        if self.command_builder._content == '':
            pass
        else:
            self.command_builder.commit()
            logger.debug( self.command_builder._content )
            self.command_builder.publish(self.device.connection)

        # refresh the command_builder
        self.command_builder = CommandBuilder()
