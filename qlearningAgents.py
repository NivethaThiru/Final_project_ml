from game import *
from learningAgents import ReinforcementAgent
from featureExtractors import *

import random,util,math
          
class QLearningAgent(ReinforcementAgent):
  """
    Q-Learning Agent
  """
  def __init__(self, **args):
    ReinforcementAgent.__init__(self, **args)

    self.qvalues = util.Counter()
  
  def getQValue(self, state, action):
    """
      Returns Q(state,action)    
      Should return 0.0 if we never seen
      a state or (state,action) tuple 
    """
    if self.qvalues.has_key((state,action)):
        return self.qvalues[(state,action)]
    else:
        self.qvalues[(state,action)] = 0.0
    return self.qvalues[(state,action)]
    util.raiseNotDefined()
  
    
  def getValue(self, state):
    """
      Returns max_action Q(state,action)        
      where the max is over legal actions.  Note that if
      there are no legal actions, which is the case at the
      terminal state, you should return a value of 0.0.
    """
    comp_list = []
    
    if len(self.getLegalActions(state)) == 0 :
        return 0.0
    
    for a in self.getLegalActions(state):
        if self.qvalues.has_key((state,a)):
            comp_list.append(self.qvalues[(state,a)])
        else:
            self.qvalues[(state,a)] = 0.0
            comp_list.append(self.qvalues[(state,a)])
                             
    return max(comp_list)
    
    util.raiseNotDefined()
    
  def getPolicy(self, state):
    """
      Compute the best action to take in a state.  Note that if there
      are no legal actions, which is the case at the terminal state,
      you should return None.
    """
    if len(self.getLegalActions(state)) ==0:
        return None
    for a in self.getLegalActions(state):
        if self.qvalues[(state,a)] == self.getValue(state):
            return a
    util.raiseNotDefined()
    
  def getAction(self, state):
    """
      Compute the action to take in the current state.  With
      probability self.epsilon, we should take a random action and
      take the best policy action otherwise.  Note that if there are
      no legal actions, which is the case at the terminal state, you
      should choose None as the action.
    """  
    # Pick Action
    legalActions = self.getLegalActions(state)
    action = None
    if len(legalActions) != 0:
        
        if util.flipCoin(self.epsilon):
            action = random.choice(legalActions)
        else:
            action = self.getPolicy(state)
    return action
    util.raiseNotDefined()
  
  def update(self, state, action, nextState, reward):
    """
      The parent class calls this to observe a 
      state = action => nextState and reward transition.
      You should do your Q-Value update here
    """
    comp_list = []
    for a in self.getLegalActions(nextState):
        if self.qvalues.has_key((nextState,a)):
            comp_list.append(self.qvalues[(nextState,a)])
        else:
            self.qvalues[(nextState,a)] = 0.0
            comp_list.append(self.qvalues[(nextState,a)])
    
    self.qvalues[(state,action)] = (1 - self.alpha) * self.qvalues[(state,action)] + self.alpha * (reward + self.gamma * self.getValue(nextState))
    #util.raiseNotDefined()