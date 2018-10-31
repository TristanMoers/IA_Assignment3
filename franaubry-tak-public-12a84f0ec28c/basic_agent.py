from agent import AlphaBetaAgent
import minimax

"""
Agent skeleton. Fill in the gaps.
"""
class MyAgent(AlphaBetaAgent):

  """
  This is the skeleton of an agent to play the Tak game.
  """
  def get_action(self, state, last_action, time_left):
    self.last_action = last_action
    self.time_left = time_left
    return minimax.search(state, self)

  """
  The successors function must return (or yield) a list of
  pairs (a, s) in which a is the action played to reach the
  state s.
  """
  def successors(self, state):
        actions = state.get_current_player_actions()
        actions_state = list()
        for action in actions:
          if state.is_action_valid(action):  
            Nstate = state.copy()
            Nstate.apply_action(action)
            actions_state.append((action, Nstate))
        for a in actions_state:
            yield a

  """
  The cutoff function returns true if the alpha-beta/minimax
  search has to stop and false otherwise.
  """
  def cutoff(self, state, depth):
    return state.game_over_check() or depth >= 1

  """
  The evaluate function must return an integer value
  representing the utility function of the board.
  """
  def evaluate(self, state):
    isOver, win = state.is_over()
    if win == self.id: 
      return 1000
    else if winn == self.id - 1:
      return -1000
      else
        return nb_ceil(self.id, state) - nb_ceil(self.id - 1, state)

def nb_ceil(id, state):
  return 0

