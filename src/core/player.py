"""
This module handles the player data and statistics.

Classes:
    Player: A class representing a player in the football league.
"""

from .team import Team

class Player:
    """
    Initializes the player.
    """
    name: str
    age: int
    position: str
    team: Team