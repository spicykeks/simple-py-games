<<<<<<< HEAD
class Game:
    def __init__(self, rounds_count = 1, player_wins = [0, 0]):
        """
        Initialization function for general game class.

        Arguments:
            rounds_count: Count of rounds to play
            player_wins: List of wins for each player, starts at 0

        Returns:
            None
        """
        self.rounds_count = rounds_count
        self.player_wins = player_wins
        self.current_round = 1

    def change_win_count(self, winner_pos):
        """
        After the end of any given round, augment the win count by 1.

        Arguments:
            winner_pos = position of the winner in the list

        Returns:
            None
        """
        self.player_wins[winner_pos-1] = self.player_wins[winner_pos-1] + 1

    def __repr__(self):
        """
        Magic method for printing a Game object

        Arguments:
            None

        Returns:
            None
        """
        
        return "Round count: {}, Player wins (1 & 2): {}".format(self.rounds_count, self.player_wins)
=======
class Game:
    def __init__(self, rounds_count = 1, player_wins = [0, 0]):
        """
        Initialization function for general game class.

        Arguments:
            rounds_count: Count of rounds to play
            player_wins: List of wins for each player, starts at 0

        Returns:
            None
        """
        self.rounds_count = rounds_count
        self.player_wins = player_wins
        self.current_round = 1

    def change_win_count(self, winner_pos):
        """
        After the end of any given round, augment the win count by 1.

        Arguments:
            winner_pos = position of the winner in the list

        Returns:
            None
        """
        self.player_wins[winner_pos-1] = self.player_wins[winner_pos-1] + 1

    def __repr__(self):
        """
        Magic method for printing a Game object

        Arguments:
            None

        Returns:
            None
        """
        
        return "Round count: {}, Player wins (1 & 2): {}".format(self.rounds_count, self.player_wins)
>>>>>>> bbdcd05a5f5cdbf5e01b147e77b9c7506c834dd1
