import time


class TicTacToe:
    def __init__(self, choice):
        self.board = [
            ['-', '-', '-'],
            ['-', '-', '-'],
            ['-', '-', '-']
        ]
        self.choice = choice

    def _win(self):
        if self.board[0][0] == 'X':
            if self.board[1][0] == 'X':
                if self.board[2][0] == 'X':
                    return True
            if self.board[1][1] == 'X':
                if self.board[2][2] == 'X':
                    return True
            if self.board[0][1] == 'X':
                if self.board[0][2] == 'X':
                    return True
        if self.board[2][0] == 'X':
            if self.board[1][1] == 'X':
                if self.board[0][2] == 'X':
                    return True
            if self.board[2][1] == 'X':
                if self.board[2][2] == 'X':
                    return True
        if self.board[1][0] == 'X':
            if self.board[1][1] == 'X':
                if self.board[1][2] == 'X':
                    return True
        if self.board[0][1] == 'X':
            if self.board[1][1] == 'X':
                if self.board[2][1] == 'X':
                    return True

        if self.board[0][0] == 'O':
            if self.board[1][0] == 'O':
                if self.board[2][0] == 'O':
                    return True
            if self.board[1][1] == 'O':
                if self.board[2][2] == 'O':
                    return True
            if self.board[0][1] == 'O':
                if self.board[0][2] == 'O':
                    return True
        if self.board[2][0] == 'O':
            if self.board[1][1] == 'O':
                if self.board[0][2] == 'O':
                    return True
            if self.board[2][1] == 'O':
                if self.board[2][2] == 'O':
                    return True
        if self.board[1][0] == 'O':
            if self.board[1][1] == 'O':
                if self.board[1][2] == 'O':
                    return True
        if self.board[0][1] == 'O':
            if self.board[1][1] == 'O':
                if self.board[2][1] == 'O':
                    return True
        return False

    def _player_turn(self):
        move = int(input("Please enter a number 1-9 to denote your spot on the board, with 1 being the top left "
                         "corner and 9 being the bottom right corner\n"))
        valid_move = False
        while not valid_move:
            if move == 1 and self.board[0][0] == '-':
                self.board[0][0] = self.choice
                valid_move = True
            elif move == 2 and self.board[0][1] == '-':
                self.board[0][1] = self.choice
                valid_move = True
            elif move == 3 and self.board[0][2] == '-':
                self.board[0][2] = self.choice
                valid_move = True
            elif move == 4 and self.board[1][0] == '-':
                self.board[1][0] = self.choice
                valid_move = True
            elif move == 5 and self.board[1][1] == '-':
                self.board[1][1] = self.choice
                valid_move = True
            elif move == 6 and self.board[1][2] == '-':
                self.board[1][2] = self.choice
                valid_move = True
            elif move == 7 and self.board[2][0] == '-':
                self.board[2][0] = self.choice
                valid_move = True
            elif move == 8 and self.board[2][1] == '-':
                self.board[2][1] = self.choice
                valid_move = True
            elif move == 9 and self.board[2][2] == '-':
                self.board[2][2] = self.choice
                valid_move = True
            else:
                move = int(input("Invalid move please try again\n"))

    def _computer_turn(self):
        if self.choice == 'X':
            computer = 'O'
        else:
            computer = 'X'

        # First check for a winning move
        if self.board[0][0] == computer:
            if self.board[0][1] == computer and self.board[0][2] == '-':
                self.board[0][2] = computer
                return
            if self.board[0][2] == computer and self.board[0][1] == '-':
                self.board[0][1] = computer
                return
            if self.board[2][2] == computer and self.board[1][1] == '-':
                self.board[1][1] = computer
                return
            if self.board[2][0] == computer and self.board[1][0] == '-':
                self.board[1][0] = computer
                return
            if self.board[1][0] == computer and self.board[2][0] == '-':
                self.board[2][0] = computer
                return
        elif self.board[1][0] == computer:
            if self.board[0][0] == computer and self.board[2][0] == '-':
                self.board[2][0] = computer
                return
            if self.board[2][0] == computer and self.board[0][0] == '-':
                self.board[0][0] = computer
                return
            if self.board[1][1] == computer and self.board[1][2] == '-':
                self.board[1][2] = computer
                return
            if self.board[1][2] == computer and self.board[1][1] == '-':
                self.board[1][1] = computer
                return
        elif self.board[2][0] == computer:
            if self.board[0][0] == computer and self.board[1][0] == '-':
                self.board[1][0] = computer
                return
            if self.board[1][0] == computer and self.board[0][0] == '-':
                self.board[0][0] = computer
                return
            if self.board[0][2] == computer and self.board[1][1] == '-':
                self.board[1][1] = computer
                return
            if self.board[2][1] == computer and self.board[2][2] == '-':
                self.board[2][2] = computer
                return
            if self.board[2][2] == computer and self.board[2][1] == '-':
                self.board[2][1] = computer
                return
        elif self.board[0][1] == computer:
            if self.board[0][0] == computer and self.board[0][2] == '-':
                self.board[0][2] = computer
                return
            if self.board[0][2] == computer and self.board[0][0] == '-':
                self.board[0][0] = computer
                return
            if self.board[2][1] == computer and self.board[1][1] == '-':
                self.board[1][1] = computer
                return
            if self.board[1][1] == computer and self.board[2][1] == '-':
                self.board[2][1] = computer
                return
        elif self.board[1][1] == computer:
            if self.board[0][0] == computer and self.board[2][2] == '-':
                self.board[2][2] = computer
                return
            if self.board[0][1] == computer and self.board[2][1] == '-':
                self.board[2][1] = computer
                return
            if self.board[0][2] == computer and self.board[2][0] == '-':
                self.board[2][0] = computer
                return
            if self.board[1][0] == computer and self.board[1][2] == '-':
                self.board[1][2] = computer
                return
            if self.board[1][2] == computer and self.board[1][0] == '-':
                self.board[1][0] = computer
                return
            if self.board[2][0] == computer and self.board[0][2] == '-':
                self.board[0][2] = computer
                return
            if self.board[2][1] == computer and self.board[0][1] == '-':
                self.board[0][1] = computer
                return
            if self.board[2][2] == computer and self.board[0][0] == '-':
                self.board[0][0] = computer
                return
        elif self.board[2][1] == computer:
            if self.board[2][0] == computer and self.board[2][2] == '-':
                self.board[2][2] = computer
                return
            if self.board[2][2] == computer and self.board[2][0] == '-':
                self.board[2][0] = computer
                return
            if self.board[0][1] == computer and self.board[1][1] == '-':
                self.board[1][1] = computer
                return
            if self.board[1][1] == computer and self.board[0][1] == '-':
                self.board[0][1] = computer
                return
        elif self.board[0][2] == computer:
            if self.board[0][0] == computer and self.board[0][1] == '-':
                self.board[0][1] = computer
                return
            if self.board[0][1] == computer and self.board[0][0] == '-':
                self.board[0][0] = computer
                return
            if self.board[1][1] == computer and self.board[2][0] == '-':
                self.board[2][0] = computer
                return
            if self.board[2][0] == computer and self.board[1][1] == '-':
                self.board[1][1] = computer
                return
            if self.board[1][2] == computer and self.board[2][2] == '-':
                self.board[2][2] = computer
                return
            if self.board[2][2] == computer and self.board[1][2] == '-':
                self.board[1][2] = computer
                return
        elif self.board[1][2] == computer:
            if self.board[1][1] == computer and self.board[1][0] == '-':
                self.board[1][0] = computer
                return
            if self.board[1][0] == computer and self.board[1][1] == '-':
                self.board[1][1] = computer
                return
            if self.board[0][2] == computer and self.board[2][2] == '-':
                self.board[2][2] = computer
                return
            if self.board[2][2] == computer and self.board[0][2] == '-':
                self.board[0][2] = computer
                return
        elif self.board[2][2] == computer:
            if self.board[1][2] == computer and self.board[0][2] == '-':
                self.board[0][2] = computer
                return
            if self.board[0][2] == computer and self.board[1][2] == '-':
                self.board[1][2] = computer
                return
            if self.board[1][1] == computer and self.board[0][0] == '-':
                self.board[0][0] = computer
                return
            if self.board[0][0] == computer and self.board[1][1] == '-':
                self.board[1][1] = computer
                return
            if self.board[2][1] == computer and self.board[2][0] == '-':
                self.board[2][0] = computer
                return
            if self.board[2][0] == computer and self.board[2][1] == '-':
                self.board[2][1] = computer
                return

        # Next we need to check for a block
        if self.board[0][0] == self.choice and self.board[0][1] == self.choice and self.board[0][2] == '-':
            self.board[0][2] = computer
            return
        elif self.board[0][0] == self.choice and self.board[0][2] == self.choice and self.board[0][1] == '-':
            self.board[0][1] = computer
            return
        elif self.board[0][1] == self.choice and self.board[0][2] == self.choice and self.board[0][0] == '-':
            self.board[0][0] = computer
            return
        elif self.board[0][0] == self.choice and self.board[2][2] == self.choice and self.board[1][1] == '-':
            self.board[1][1] = computer
            return
        elif self.board[0][0] == self.choice and self.board[1][1] == self.choice and self.board[2][2] == '-':
            self.board[2][2] = computer
            return
        elif self.board[0][0] == self.choice and self.board[1][0] == self.choice and self.board[2][0] == '-':
            self.board[2][0] = computer
            return
        elif self.board[0][0] == self.choice and self.board[2][0] == self.choice and self.board[1][0] == '-':
            self.board[1][0] = computer
            return
        elif self.board[0][1] == self.choice and self.board[1][1] == self.choice and self.board[2][1] == '-':
            self.board[2][1] = computer
            return
        elif self.board[0][1] == self.choice and self.board[2][1] == self.choice and self.board[1][1] == '-':
            self.board[1][1] = computer
            return
        elif self.board[0][2] == self.choice and self.board[1][1] == self.choice and self.board[2][0] == '-':
            self.board[2][0] = computer
            return
        elif self.board[0][2] == self.choice and self.board[2][0] == self.choice and self.board[1][1] == '-':
            self.board[1][1] = computer
            return
        elif self.board[0][2] == self.choice and self.board[1][2] == self.choice and self.board[2][2] == '-':
            self.board[2][2] = computer
            return
        elif self.board[0][2] == self.choice and self.board[2][2] == self.choice and self.board[1][2] == '-':
            self.board[1][2] = computer
            return
        elif self.board[1][0] == self.choice and self.board[2][0] == self.choice and self.board[0][0] == '-':
            self.board[0][0] = computer
            return
        elif self.board[1][0] == self.choice and self.board[1][1] == self.choice and self.board[1][2] == '-':
            self.board[1][2] = computer
            return
        elif self.board[1][0] == self.choice and self.board[1][2] == self.choice and self.board[1][1] == '-':
            self.board[1][1] = computer
            return
        elif self.board[1][1] == self.choice and self.board[1][2] == self.choice and self.board[1][0] == '-':
            self.board[1][0] = computer
            return
        elif self.board[1][1] == self.choice and self.board[2][2] == self.choice and self.board[0][0] == '-':
            self.board[0][0] = computer
            return
        elif self.board[1][1] == self.choice and self.board[2][0] == self.choice and self.board[0][2] == '-':
            self.board[0][2] = computer
            return
        elif self.board[1][1] == self.choice and self.board[2][1] == self.choice and self.board[0][1] == '-':
            self.board[0][1] = computer
            return
        elif self.board[1][2] == self.choice and self.board[2][2] == self.choice and self.board[0][2] == '-':
            self.board[0][2] = computer
            return
        elif self.board[2][0] == self.choice and self.board[2][1] == self.choice and self.board[2][2] == '-':
            self.board[2][2] = computer
            return
        elif self.board[2][0] == self.choice and self.board[2][2] == self.choice and self.board[2][1] == '-':
            self.board[2][1] = computer
            return
        elif self.board[2][1] == self.choice and self.board[2][2] == self.choice and self.board[2][0] == '-':
            self.board[2][0] = computer
            return

        # Next we fork if possible
        if self.board[0][0] == computer and self.board[2][2] == computer:
            if self.board[1][2] == '-' and self.board[0][1] == '-':
                self.board[0][2] = computer
                return
            if self.board[2][1] == '-' and self.board[1][0] == '-':
                self.board[2][0] = computer
                return
        elif self.board[0][2] == computer and self.board[2][2] == computer:
            if self.board[1][1] == '-' and self.board[0][1] == '-':
                self.board[0][0] = computer
                return
            if self.board[0][0] == '-' and self.board[2][0] == '-':
                self.board[1][1] = computer
                return
        elif self.board[0][2] == computer and self.board[2][0] == computer:
            if self.board[0][1] == '-' and self.board[1][0] == '-':
                self.board[0][0] = computer
                return
            if self.board[2][1] == '-' and self.board[1][2] == '-':
                self.board[2][2] = computer
                return
        elif self.board[0][0] == computer and self.board[1][1] == computer:
            if self.board[0][1] == '-' and self.board[2][0] == '-':
                self.board[0][2] = computer
                return
            if self.board[0][2] == '-' and self.board[1][0] == '-':
                self.board[2][0] = computer
                return

        # Next we block a fork if we can
        if self.board[0][0] == self.choice and self.board[2][2] == self.choice:
            if self.board[0][2] == '-':
                self.board[0][2] = computer
                return
            if self.board[2][0] == '-':
                self.board[2][0] = computer
        if self.board[0][2] == self.choice and self.board[2][0] == self.choice:
            if self.board[0][0] == '-':
                self.board[0][0] = computer
                return
            if self.board[2][2] == '-':
                self.board[2][2] = computer

        # Next we play the center if available
        if self.board[1][1] == '-':
            self.board[1][1] = computer
            return

        # Next if the oppenent is in the corner we will take the opposite corner
        if self.board[0][0] == self.choice and self.board[2][2] == '-':
            self.board[2][2] = computer
            return
        elif self.board[2][2] == self.choice and self.board[0][0] == '-':
            self.board[0][0] = computer
            return
        elif self.board[2][0] == self.choice and self.board[0][2] == '-':
            self.board[0][2] = computer
            return
        elif self.board[0][2] == self.choice and self.board[2][0] == '-':
            self.board[2][0] = computer
            return

        # Next we will take an empty corner
        if self.board[0][0] == '-':
            self.board[0][0] = computer
            return
        elif self.board[0][2] == '-':
            self.board[0][2] = computer
            return
        elif self.board[2][0] == '-':
            self.board[2][0] = computer
            return
        elif self.board[2][2] == '-':
            self.board[2][2] = computer
            return

        # Next we will take an empty side
        if self.board[0][1] == '-':
            self.board[0][1] = computer
            return
        elif self.board[1][2] == '-':
            self.board[1][2] = computer
            return
        elif self.board[2][1] == '-':
            self.board[2][1] = computer
            return
        elif self.board[1][0] == '-':
            self.board[1][0] = computer
            return

    def _print_board(self):
        for i in self.board:
            print(i)

    def play_game(self):
        if self.choice == 'X':
            while not self._win():
                self._print_board()
                if self._win():
                    print("Computer wins!")
                    break
                self._player_turn()
                self._print_board()
                if self._win():
                    print("Player wins!")
                    break
                print("Computer's turn!")
                time.sleep(2)
                self._computer_turn()
        else:
            while not self._win():
                print("Computer's turn!")
                time.sleep(2)
                self._computer_turn()
                self._print_board()
                if self._win():
                    print("Computer wins!")
                    break
                self._player_turn()
                self._print_board()
                if self._win():
                    print("Player wins!")
                    break


if __name__ == '__main__':
    player = input("Please input X or O to designate which position you'd like to play!\n").upper()
    ttt = TicTacToe(player)
    ttt.play_game()
