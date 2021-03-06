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
      for action in actions:
          Nstate = state.copy()
          Nstate.apply_action(action)
          yield (action, Nstate)

  """
  The cutoff function returns true if the alpha-beta/minimax
  search has to stop and false otherwise.
  """
  def cutoff(self, state, depth):
    return state.game_over_check() or depth == 2

  """
  The evaluate function must return an integer value
  representing the utility function of the board.
  """
  def evaluate(self, state):
    isOver, win = state.is_over()
    if isOver:
        if state.get_winner() == self.id:
            return 1000
        elif state.get_winner() == 1 - self.id:
            return -1000
    else:
        return state.control_count()[self.id] - state.control_count()[1-self.id]

