class TicTacToeView:
    def display_board(self, board):
        print("-------------")
        for i in range(0, 9, 3):
            print(f"| {board[i]} | {board[i+1]} | {board[i+2]} |")
            print("-------------")

    def get_player_move(self, player: int):
        while True:
            try:
                move = int(input(f"Player {player}, enter your move (0-8): "))
                return move
            except ValueError:
                print("Invalid input. Please enter a number between 0 and 8.")

    def display_winner(self, winner):
        if winner == 'DRAW':
            print("It's a draw!")
        else:
            print(f"Player {winner} wins!")

    def display_invalid_move(self):
        print("Invalid move. Please try again.")

    def display_game_over(self):
        print("Game over.")