from .Games import Game

class TTT(Game):

    def __init__(self, rounds_count, player_wins):
        """Initialization function for Rock Paper Scissors

        Arguments:
            rounds_count: Number of rounds to play
            player_wins: List of rounds won for each player
        """
        Game.__init__(self, rounds_count, player_wins)
        self.board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    def printBoard(self):
        print("| {} | {} | {}".format(self.board[0], self.board[1], self.board[2]))
        print("______________")
        print("| {} | {} | {}".format(self.board[3], self.board[4], self.board[5]))
        print("______________")
        print("| {} | {} | {}".format(self.board[6], self.board[7], self.board[8]))

    def play(self):
        print("Player 1 always starts with X. Try playing Rock Paper Scissors to see who goes first!")
        print("Player 2 places O.")
        while not (self.boardFull()):

            while True:
                move_one = input("Player one: Please enter a number from 1-9: ")
                if move_one not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    continue
                else:
                    move_one = int(move_one)
                    if self.isFree(move_one-1):
                        break
                    else:
                        print("That spot is taken!")
                        continue
            self.placeLetter(move_one - 1, "X")

            self.printBoard()

            while True:
                move_two = input("Please enter a number from 1-9: ")
                if move_two not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    continue
                else:
                    move_two = int(move_two)
                    if self.isFree(move_two-1):
                        break
                    else:
                        print("That spot is taken!")
                        continue
            self.placeLetter(move_two - 1, "O")

            self.printBoard();

            if self.isWinner("X"):
                print("Player 1 wins!")
                break
            elif self.isWinner("O"):
                print("Player 2 wins!")
                break
            else:
                continue

    def placeLetter(self, move, letter):
        self.board[move] = letter

    def isFree(self, move):
        return self.board[move] == ' '

    def boardFull(self):
        for i in range(9):
            if self.board[i] == ' ':
                return False
        return True

    def isWinner (self, letter):
        return ((([letter.upper()] * 3) == (self.board[0], self.board[1], self.board[2])) or
         (([letter.upper()]) * 3 == (self.board[3], self.board[4], self.board[5])) or
         (([letter.upper()]) * 3 == (self.board[6], self.board[7], self.board[8])) or
         (([letter.upper()]) * 3 == (self.board[0], self.board[3], self.board[6])) or
         (([letter.upper()]) * 3 == (self.board[1], self.board[4], self.board[7])) or
         (([letter.upper()]) * 3 == (self.board[2], self.board[5], self.board[8])) or
         (([letter.upper()]) * 3 == (self.board[0], self.board[4], self.board[8])) or
         (([letter.upper()]) * 3 == (self.board[2], self.board[4], self.board[6])))
