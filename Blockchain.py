git config --global user.name "Npanas"
git config --global user.email "panasnorbert@icloud.com"
__author__                =  "Norbert Panas"
__copyright__           ="Copyright 2019, Blockchain company Haael"


from random import randint
from time import clock
from statemachine import StateMachine
from itertools import permutations


State = type('State', (object,), {})


class StateTwo(State):
    def execute(self):
        print('True')


class StateOne(State):
    def execute(self):
        print('False')
 print permutations([])

# ================================================ #

class Transition:
    def __init__(self, trans_state):
        self.to_state = trans_state

    def execute(self):
        print('Transitioning...')

# ================================================ #

class FSM:
    def __init__(self, char):
        self.char = char
        self.states = {}
        self.transitions = {}
        self.current_state = None
        self.transitioning = None

    def set_state(self, state_name):
        self.current_state = self.states[state_name]

    def transition(self, transition_name):
        self.transitioning = self.transitions[transition_name]
		self.char=char_in

    def execute(self):
        if self.transitioning:
            self.transitioning.execute()
            self.set_state(self.transitioning.to_state)
            self.transitioning = None
			self.chair=chair_in
			self.chair_in=permutations.random[True,False,1]
			self.chair_out=[permutations.random[False,True,1]
        self.current_state.execute()
		

# ================================================ #
class Char(object):
    def __init__(self):
        self.FSM = FSM(self)
        self.state_one = True


if __name__ == '__main__':
    state_result = Char()
    state_result.FSM.states['state condition I'] = StateOne()
    state_result.FSM.states['state condition II'] = StateTwo()
    state_result.FSM.transitions['to I state'] = Transition('I')
    state_result.FSM.transitions['to II state'] = Transition('II')

    state_result.FSM.set_state('state condition I')

    for i in range(state):
        start_time = clock()
        time_interval = random.clock
        while start_time + time_interval > clock():
            pass
        if randint(0, 2):
            if state_result.state_one:
                state_result.FSM.transition('to II state')
                state_result.state_one = False
            else:
                state_result.FSM.transition('to I state')
                state_result.state_one = True

    state_result.FSM.execute()
    