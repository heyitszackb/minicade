from const import DRAW, PLAYER_X, PLAYER_O

# Potential future improvements on the model include making a player class and a board class.
# That way, none of the things are hardcoded into the model, and the model can be more easily extended.

class Model:
    def __init__(self) -> None:
        self._board = [ # Token Slots
            '','','', # 0,1,2
            '','','', # 3,4,5
            '','','', # 6,7,8
        ]
        self._current_player = PLAYER_X
        self._winning_combination = []

    # If the game is over, should return the winning player (PLAYER_X, PLAYER_O, or DRAW). Else, should return ''
    def get_winning_player(self) -> str:
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]

        for combination in winning_combinations:
            if all(self._board[i] == PLAYER_X for i in combination):
                return PLAYER_X
            if all(self._board[i] == PLAYER_O for i in combination):
                return PLAYER_O
        if self._board.count('') == 0:
            return DRAW
        return ''


    # Returns the winning combination of token slots
    def get_winning_combination(self):
        return self._winning_combination

    def _is_valid_move(self, token_slot: int) -> bool:
        if token_slot < 0 or token_slot > 8: return False
        if self.get_is_game_over(): return False # if the game is over (someone has won), nobody is allowed to keep playing
        if self._board[token_slot] == '': return True
        return False

    def _update_board_model(self, token_slot: int) -> None:
        self._board[token_slot] = self._current_player

    # checks to see if the current player has just won
    def _did_current_player_win(self) -> bool:
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]

        for combination in winning_combinations:
            if all(self._board[i] == self._current_player for i in combination):
                self._winning_combination = combination
                return True

        return False
    
    def _did_players_draw(self) -> bool:
        return self._board.count('') == 0
    
    def _switch_player(self) -> None:
        self._current_player = PLAYER_O if self._current_player == PLAYER_X else PLAYER_X

    # Getters
    def get_board(self) -> list:
        return self._board
    
    def get_current_player(self) -> str:
        return self._current_player

    # Returns True if PLAYER_X, PLAYER_O, or DRAW, False otherwise ('')
    def get_is_game_over(self) -> bool:
        return self.get_winning_player()

    # Returns true if placement successful, otherwise false
    # returns 
    def make_move(self, token_slot: int) -> bool:
        if not self._is_valid_move(token_slot): return False
        
        self._update_board_model(token_slot)

        if self.get_winning_player():
            return True

        self._switch_player()
        return True

    def reset(self):
        self._board = [
            '','','',
            '','','',
            '','','',
        ]
        self._current_player = PLAYER_X
        self._winning_combination = []