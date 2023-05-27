
# Import whatever Library classes you need - Model is obviously needed
import time
import random
from Model import *
from Button import *
from Counters import *
from Displays import *

class StopWatch:

    def __init__(self):
        
        # Instantiate whatever classes from your own model that you need to control
        self._startbutton = Button(0, "startbutton", buttonhandler=self)
        self._stopbutton = Button(13, "stopbutton", buttonhandler=self)
        self._display = LCDDisplay(sda=20, scl=21, i2cid=0)
        self._t1 = TimeKeeper()
        self._t2 = TimeKeeper()
        
        # Instantiate a Model. Needs to have the number of states, self as the handler
        # You can also say debug=True to see some of the transitions on the screen
        # Here is a sample for a model with 4 states
        self._model = Model(4, self, debug=True)
        
        # Now add all the transitions that are supported by my Model
        # obvously you only have BTN1_PRESS through BTN4_PRESS
        # BTN1_RELEASE through BTN4_RELEASE
        # and TIMEOUT
        
        # some examples:
        self._model.addTransition(0, BTN1_PRESS, 1)
        self._model.addTransition(1, BTN1_PRESS, 3)
        self._model.addTransition(2, BTN1_PRESS, 1)
        self._model.addTransition(3, BTN1_PRESS, 3)

        self._model.addTransition(1, BTN2_PRESS, 2)
        self._model.addTransition(2, BTN2_PRESS, 0)
        self._model.addTransition(3, BTN2_PRESS, 2)



        # etc.
    

def run(self):
        # The run method should first start the model
    self._Model.start()

        # Then it should do a continous loop while the model runs
    while self._model._running:
            # Inside, you can use if statements do handle various do/actions
            # that you need to perform for each state
            # Do not perform entry and exit actions here - those are separate
            
            # You can see which state the model is in (yeah i know)
                curstate = self._model._curState
            
            # Now if you want to do different things for each state you can do it:
    if curstate == 1:
                # State 0 do/actions
                self._display.showText(str(self._t1),0,0)
                self._display.showText(str(self._t2),1,0)
                
    elif curstate == 3:
                # State1 do/actions
                # You can check your sensors here and perform transitions manually if needed
                # For example, if you want to go from state 1 to state 2 when the motion sensor
                # is tripped you can do something like this
                # if self.motionsensor.tripped():
                #   gotoState(2)
                self._display.showText(str(self._t1),0,0)
                self._display.showText(str(self._t2),1,0)              
            
            #etc.

            # If you are using a software timer, you will need to do a poll to
            # see if the timer has timed out. Hardware timer does not need polling
            # Note that Wokwi does not do well with Hardware timers
            
            # self._timer.check()
            
            # I suggest putting in a short wait so you are not overloading the poor Pico
    time.sleep(0.1)


def stateEntered(self, state):
        # Again if statements to do whatever entry/actions you need
        if state == 0:
            # entry actions for state 0
            print('State 0 entered')
            self._t1.reset()
            self._t2.reset()
            self._display.reset()
            pass
        
        elif state == 1:
            # entry actions for state 1
            print('State 1 entered')
            self._t1.start()
            self._t2.start()
            self._timer.start(5)
        
        elif state == 2:
            # entry actions for state 1
            print('State 2 entered')
            self._t1.stop()
            self._t2.stop()
            self._timer.start(5)

        elif state == 3:
            # entry actions for state 1
            print('State 3 entered')
            self._t2.reset()
            self._timer.start(5)     



def stateLeft(self, state):
        pass

    

def buttonPressed(self, name):
        # For example, lets say the start button is BTN1 and stop button is BTN2
        if name == "startbutton":
            self._model.processEvent(BTN1_PRESS)
        # if you have multiple buttons, feel free to add them. Up to 4 buttons
        # are supported by the model right now.
        elif name == "stopbutton":
            self._model.processEvent(BTN2_PRESS)

def buttonReleased(self, name):
        pass




def timeout(self):
        self._model.processEvent(TIMEOUT)
        

# Test your model. Note that this only runs the template class above
# If you are using a separate main.py or other control script,
# you will run your model from there.
        if _name_ == '__main__':
            MyControllerTemplate().run()
