from const import DRAW, PLAYER_X, PLAYER_O

class TicTacToe:
    def __init__(self) -> None:
        self._board = [ # Token Slots
            '','','', # 0,1,2
            '','','', # 3,4,5
            '','','', # 6,7,8
        ]
        self._winning_player = ''
        self._current_player = PLAYER_X
        self._is_game_over = False

    def _is_valid_move(self, token_slot: int) -> bool:
        if token_slot < 0 or token_slot > 8: return False
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
                return True

        return False
    
    def _did_players_draw(self) -> bool:
        return self._board.count('') == 0
    
    def _switch_player(self) -> None:
        self._current_player = PLAYER_O if self._current_player == PLAYER_X else PLAYER_X

    def _handle_end_game(self, winner: str) -> None:
        self._is_game_over = True
        self._winning_player = winner

    # Getters
    def get_board(self) -> list:
        return self._board
    
    def get_current_player(self) -> str:
        return self._current_player
    
    def get_winning_player(self) -> str:
        return self._winning_player

    def get_is_game_over(self) -> bool:
        return self._is_game_over

    # Returns true if placement successful, otherwise false
    # returns 
    def make_move(self, token_slot: int) -> bool:
        if not self._is_valid_move(token_slot): return False
        
        self._update_board_model(token_slot)

        if self._did_current_player_win():
            self._handle_end_game(self._current_player)
            return True
        
        if self._did_players_draw():
            self._handle_end_game(DRAW)
            return True

        self._switch_player()
        return True

    def reset(self):
        self.board = [
            '','','',
            '','','',
            '','','',
        ]
        self._winning_player = ''
        self._current_player = PLAYER_X
        self._is_game_over = False