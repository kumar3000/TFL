"""
This module handles team data and statistics.

Classes:
    Team: A class representing a team in the football league.
"""

class Team:
    """
    Initializes the team.

    Functions:
        __init__(self, name: str, city: str, year: int): Initializes the team.
        add_win(self): Adds a win to the team.
        get_wins(self) -> int: Returns the number of wins.
        add_loss(self): Adds a loss to the team.
        get_losses(self) -> int: Returns the number of losses.
        add_tie(self): Adds a tie to the team.
        get_ties(self) -> int: Returns the number of ties.
        get_name(self) -> str: Returns the name of the team.
        get_year(self) -> int: Returns the year of the team.
        get_seasons(self) -> int: Returns the number of seasons.
        add_year(self): Adds a year to the team.
        get_record(self) -> str: Returns the record of the team.
    """
    name: str
    city: str
    wins: int
    losses: int
    ties: int
    year: int
    seasons: int

    def __init__(self, name: str, city: str, year: int):
        """
        Initializes the team.

        Args:
            name: str: The name of the team.
            city: str: The city of the team.
            year: int: The year of the team.
        """

        self.name = name
        self.city = city
        self.year = year
        self.seasons = 0
        self.wins = 0
        self.losses = 0
        self.ties = 0

    def add_win(self):
        """
        Adds a win to the team.
        """

        self.wins += 1

    def get_wins(self) -> int:
        """
        Returns the number of wins.
        
        Args:
            None

        Returns:
            int: The number of wins.
        """

        return self.wins

    def add_loss(self):
        """
        Adds a loss to the team.
        """

        self.losses += 1

    def get_losses(self) -> int:
        """
        Returns the number of losses.

        Args:
            None

        Returns:
            int: The number of losses.
        """

        return self.losses

    def add_tie(self):
        """
        Adds a tie to the team.
        """

        self.ties += 1

    def get_name(self) -> str:
        """
        Returns the name of the team.

        Args:
            None

        Returns:
            str: The name of the team.
        """

        return f"{self.city} {self.name}"

    def get_year(self) -> int:
        """
        Returns the year of the team.

        Args:
            None

        Returns:
            int: The year of the team.
        """

        return self.year

    def get_seasons(self) -> int:
        """
        Returns the number of seasons.

        Args:
            None

        Returns:
            int: The number of seasons.
        """

        return self.seasons

    def add_year(self):
        """
        Adds a year to the team.
        """

        self.year += 1
        self.seasons += 1

    def get_record(self) -> str:
        """
        Returns the record of the team.

        Args:
            None

        Returns:
            str: The record of the team.
        """

        if self.ties > 0:
            return f"{self.wins}-{self.losses}-{self.ties}"

        return f"{self.wins}-{self.losses}"
