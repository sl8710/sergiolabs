# Import whatever Library classes you need - Model is obviously needed
import time
import random
from Model import *
from Button import *
from Counters import *
from Lights import *
from Sensors import *

class RoomController:
    def __init__(self):
        
        # Instantiate whatever classes from your own model that you need to control
        # Handlers can now be set to None - we will add them to the model and it will
        # do the handling
        self._button1 = Button(1, "lightswitch", buttonhandler=None)
        self._button2 = Button(21, "partyswitch", buttonhandler=None)
        self._pir = Sensors(28)
        self._light = Light(17)
        self._roomlight = Light(2) 
        
        
        #self._timer = SoftwareTimer(None)
        
        # Instantiate a Model. Needs to have the number of states, self as the handler
        # You can also say debug=True to see some of the transitions on the screen
        # Here is a sample for a model with 4 states
        self._model = Model(3, self, debug=True)
        
        # Up to 4 buttons and a timer can be added to the model for use in transitions
        # Buttons must be added in the sequence you want them used. The first button
        # added will respond to BTN1_PRESS and BTN1_RELEASE, for example
        self._model.addButton(self._button1)
        self._model.addButton(self._button2)
        # add other buttons (up to 3 more) if needed
        
        # Add any timer you have.
        
        
        # Now add all the transitions that are supported by my Model
        # obvously you only have BTN1_PRESS through BTN4_PRESS
        # BTN1_RELEASE through BTN4_RELEASE
        # and TIMEOUT
        
        
        #work state
        self._model.addTransition(1, BTN1_PRESS, 0)
        self._model.addTransition(1, BTN2_PRESS, 2)
        # party state
        self._model.addTransition(2, BTN1_PRESS, 1)
        self._model.addTransition(2, BTN2_PRESS, 1)
        
        # dark state
        self._model.addTransition(0, BTN1_PRESS, 1)
        self._model.addTransition(0, BTN2_PRESS, 2)
       
    
    def run(self):
        # The run method should simply do any initializations (if needed)
        # and then call the model's run method.
        # You can send a delay as a parameter if you want something other
        # than the default 0.1s. e.g.,  self._model.run(0.25)
        self._model.run()
    """
    stateDo - the method that handles the do/actions for each state
    """
    def stateDo(self, state):
            
        # Now if you want to do different things for each state you can do it:
        if state == 0:
            if self._pir.motionDetected():
                self._model.gotoState(1) 
        elif state == 2:
            # State 2 do/actions
            self._partylight.disco()
        
       
    def stateEntered(self, state):
        # Again if statements to do whatever entry/actions you need
        if state == 0:
            # entry actions for state 0
            print('State 0 entered')
            self._roomlight.off()
            self._light.off()
    
        
        elif state == 1:
            # entry actions for state 1
            print('State 1 entered')
            self._roomlight.on()
           
        elif state == 2:
            # entry actions for state 2
            print('State 2 entered')
            self._light.off()
           
        
            
    def stateLeft(self, state):
        print(f"Leaving state {state}")
        if state == 2:
            self._partylight.off()
    
# Test your model. Note that this only runs the template class above
# If you are using a separate main.py or other control script,
# you will run your model from there.

if __name__ == '__main__':
    MyControllerTemplate().run()