import time

BTN1_PRESS = 0
BTN1_RELEASE = 1
BTN2_PRESS = 2
BTN2_RELEASE = 3
BTN3_PRESS = 4
BTN3_RELEASE = 5
BTN4_PRESS = 6
BTN4_RELEASE = 7
TIMEOUT = 8
NUMEVENTS = 9
EVENTNAMES = ["BTN1_PRESS", "BTN1_RELEASE", "BTN2_PRESS","BTN2_RELEASE",
                "BTN3_PRESS", "BTN3_RELEASE", "BTN4_PRESS","BTN4_RELEASE",
                "TIMEOUT"]
class Model:
      
    def __init__(self, numstates, handler, debug=False):
               
        self._numstates = numstates
        self._running = False
        self._transitions = []
        for i in range(0, numstates):
            self._transitions.append([None]*NUMEVENTS)
        self._curState = -1
        self._handler = handler
        self._debug = debug
        self._buttons = []
        self._timer = None
    def addTransition(self, fromState, event, toState):
                
        self._transitions[fromState][event] = toState
    
    def start(self):
                
        self._curState = 0
        self._running = True
        self._handler.stateEntered(self._curState)  # start the state model
    def stop(self):
            
        if self._running:
            self._handler.stateLeft(self._curState)
        self._running = False
        self._curState = -1
    def gotoState(self, newState):
               
        if (newState < self._numstates):
            if self._debug:
                print(f"Going from State {self._curState} to State {newState}")
            self._handler.stateLeft(self._curState)
            self._curState = newState
            self._handler.stateEntered(self._curState)
    def processEvent(self, event):
                
        if (event < NUMEVENTS):
            newstate = self._transitions[self._curState][event]
            if newstate is None:
                if self._debug:
                    print(f"Ignoring event {EVENTNAMES[event]}")
            else:
                if self._debug:
                    print(f"Processing event {EVENTNAMES[event]}")
                self.gotoState(self._transitions[self._curState][event])
    def run(self, delay=0.1):        
        # Start the model first
        self.start()
        # Then it should do a continous loop while the model runs
        while self._running:
            # Inside, you can use if statements do handle various do/actions
            # that you need to perform for each state
            # Do not perform entry and exit actions here - those are separate
                        
            self._handler.stateDo(self._curState)
            
            # Ping the timer if it is a software timer
            if self._timer is not None and type(self._timer).__name__ == 'SoftwareTimer':
                self._timer.check()
            
            # I suggest putting in a short wait so you are not overloading the poor Pico
            if delay > 0:
                time.sleep(delay)
    def addButton(self, btn):
        if len(self._buttons) < 4:
            btn.setHandler(self)
            self._buttons.append(btn)
        else:
            raise ValueError('Currently we only support up to 4 buttons')
    def buttonPressed(self, name):
        """ 
        The internal button handler - now Model can take care of buttons
        that have been added using the addButton method.
        """
        for i in range(0,len(self._buttons)):
            if name == self._buttons[i]._name:
                if i == 0:
                    self.processEvent(BTN1_PRESS)
                elif i == 1:
                    self.processEvent(BTN2_PRESS)
                elif i == 2:
                    self.processEvent(BTN3_PRESS)
                elif i == 3:
                    self.processEvent(BTN4_PRESS)
      def buttonReleased(self, name):
        for i in range(0,len(self._buttons)):
            if name == self._buttons[i]._name:
                if i == 0:
                    self.processEvent(BTN1_RELEASE)
                elif i == 1:
                    self.processEvent(BTN2_RELEASE)
                elif i == 2:
                    self.processEvent(BTN3_RELEASE)
                elif i == 3:
                    self.processEvent(BTN4_RELEASE)
    def addTimer(self, timer):
        self._timer = timer
        self._timer.setHandler(self)
        def timeout(self):
        self.processEvent(TIMEOUT)
