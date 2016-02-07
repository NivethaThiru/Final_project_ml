import mdp, util

from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
  """
      * Please read learningAgents.py before reading this.*

      A ValueIterationAgent takes a Markov decision process
      (see mdp.py) on initialization and runs value iteration
      for a given number of iterations using the supplied
      discount factor.
  """
  def __init__(self, mdp, discount = 0.9, iterations = 100):
    """
      Your value iteration agent should take an mdp on
      construction, run the indicated number of iterations
      and then act according to the resulting policy.
    
      Some useful mdp methods you will use:
          mdp.getStates()
          mdp.getPossibleActions(state)
          mdp.getTransitionStatesAndProbs(state, action)
          mdp.getReward(state, action, nextState)
    """
    self.mdp = mdp
    self.discount = discount
    self.iterations = iterations
    self.values = util.Counter() # A Counter is a dict with default 0
     
    "*** YOUR CODE HERE ***"
    for s in mdp.getStates():
        self.values[s] = 0
    "for a in mdp.getPossibleActions(s):"
    "for ac in mdp.getTransitionStatesAndProbs(s,a):"
    " print ac[0]"
    "print ac[1]"
    "copy_value = self.values.copy()"
    "for c in mdp.getStates():"
    "   print copy_value[c]"
    i=0
    "self.states = mdp.getStates()"
    while i < iterations:
        copy_value = self.values.copy()
        for s in mdp.getStates():
            if not mdp.isTerminal(s):
                self.values[s] = mdp.getReward(s,'north',s) + discount * max([sum([copy_value[s1] * p for (s1,p) in mdp.getTransitionStatesAndProbs(s,a)]) for a in mdp.getPossibleActions(s)])
        i = i + 1
  
  
  def getValue(self, state):
    """
      Return the value of the state (computed in __init__).
    """
    return self.values[state]


  def getQValue(self, state, action):
    """
      The q-value of the state action pair
      (after the indicated number of value iteration
      passes).  Note that value iteration does not
      necessarily create this quantity and you may have
      to derive it on the fly.
    """
    "*** YOUR CODE HERE ***"
    return self.values[state]
    util.raiseNotDefined()

  def getPolicy(self, state):
    """
      The policy is the best action in the given state
      according to the values computed by value iteration.
      You may break ties any way you see fit.  Note that if
      there are no legal actions, which is the case at the
      terminal state, you should return None.
    """
    "*** YOUR CODE HERE ***"
    if not self.mdp.isTerminal(state):
        pi = max([sum([p * self.values[state] for (s1,p) in self.mdp.getTransitionStatesAndProbs(state,a)]) for a in self.mdp.getPossibleActions(state)])
        return pi
    return None
    util.raiseNotDefined()

  def getAction(self, state):
    "Returns the policy at the state (no exploration)."
    return self.getPolicy(state)
  
