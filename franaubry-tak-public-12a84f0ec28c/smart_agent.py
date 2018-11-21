from agent import AlphaBetaAgent
import minimax

"""
Agent skeleton. Fill in the gaps.
"""
class MyAgent(AlphaBetaAgent):

  prev_state = None

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
    return state.game_over_check() or depth == 1

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

        """return state.control_count()[self.id] - state.control_count()[1-self.id] + self.strategy1(state)"""
        return self.strategy1(state)

  def strategy1(self, state):
    count = 0
    grid = state.board

    for i in range(0,4):
        count_row = 0
        count_row_adv = 0
        count_col = 0
        count_col_adv = 0
        for j in range(0,4):
            if state.is_controlled_by(i, j, self.id):
                count_row = count_row +1
                t = state.get_top_piece(i, j)
                if t is not None:
                    if t[0] == 2 and not self.has_cap_stone_prev():
                        count_row = count_row + 20
                if i == 2 and j == 2 and self.prev_state is not None:
                    if not self.prev_state.is_controlled_by(i, j, self.id):
                        count_row = count_row + 10
            if state.is_controlled_by(i, j, 1-self.id):
                count_row_adv += 1
            if state.is_controlled_by(j, i, self.id):
                count_col = count_col + 1
                t = state.get_top_piece(i, j)
                if t is not None:
                    if t[0] == 2 and not self.has_cap_stone_prev():
                        count_col = count_col + 20
                if i == 2 and j == 2 and self.prev_state is not None:
                    if not self.prev_state.is_controlled_by(i, j, self.id):
                        count_col = count_col + 10
            if state.is_controlled_by(j, i, 1-self.id):
                count_col_adv += 1
            if count_row_adv > count_row:
                for k in range (0,4):
                    t = state.get_top_piece(i, k)
                    if t is not None:
                        if state.is_controlled_by(i, k, self) and t[0] == 1:
                            count_row += 5
                            print("youlou defense")
            if count_col_adv > count_col:
                for k in range(0,4):
                    t = state.get_top_piece(k, i)
                    if t is not None:
                        if state.is_controlled_by(k, i, self) and t[0] == 1:
                            count_col += 5
                            print("youlou defense")
        if count_row > count:
            count = count_row
        if count_col > count:
            count = count_col
    print(count)
    self.prev_state = state
    return count

  def has_cap_stone_prev(self):
    for i in range(0, 4):
        for j in range(0, 4):
            if self.prev_state is not None:
                t_prev = self.prev_state.get_top_piece(i, j)
                if t_prev is not None:
                    if t_prev[0] == 2:
                        return True
    return False
