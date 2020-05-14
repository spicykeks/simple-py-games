from .Games import Game
from getpass import getpass

class RPS(Game):

    def __init__(self, rounds_count, player_wins):
        """Initialization function for Rock Paper Scissors

        Arguments:
            rounds_count: Number of rounds to play
            player_wins: Array (IMPORTANT) of rounds won for each player
        """
        Game.__init__(self, rounds_count, player_wins)

    def play(self):
        """Function to actually play the game

        Arguments:
            None

        Returns:
            None
        """
        for i in range(self.rounds_count):
            #Loop which iterates through each round, taking input until it is valid
            #Input process could be modularized.
            while True:
                choice_one = getpass("Player 1, pick R, P or S: ")
                if choice_one.lower() not in ('r', 'p', 's'):
                    print("Sorry, your input was not valid!")
                    continue
                else:
                    break

            while True:
                choice_two = getpass("Player 1, pick R, P or S: ")
                if choice_two.lower() not in ('r', 'p', 's'):
                    print("Sorry, your input was not valid!")
                    continue
                else:
                    break
            print ("The winner of round {} is ... Player {}".format(i + 1, self.find_winner(choice_one, choice_two)))
        print("Final score: {}".format(self.player_wins))

    def find_winner(self, choice_one, choice_two):

        if choice_one.lower() == choice_two.lower():
            return None
        elif choice_one.lower() == 'r':
            if choice_two.lower() == 'p':
                self.change_win_count(2)
                return 2
            elif choice_two.lower() == 's':
                self.change_win_count(1)
                return 1

        elif choice_one.lower() == 'p':
            if choice_two.lower() == 's':
                self.change_win_count(2)
                return 2
            elif choice_two.lower() == 'r':
                self.change_win_count(1)
                return 1

        elif choice_one.lower() == 's':
            if choice_two.lower() == 'r':
                self.change_win_count(2)
                return 2
            elif choice_two.lower() == 'p':
                self.change_win_count(1)
                return 1
