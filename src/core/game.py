"""
This module handles the game simulation.

Functions:
    score(): Generates a random score for the game.
    start_game(team: Team): Starts a game and returns the score and result.
    tieless_game(team: Team): Starts a game and returns the score and result, 
                              but does not count ties.
"""

import random
from .team import Team

def score() -> tuple[int, int]:
    """
    Returns a tuple of the score for the team and the score against the team.

    Args:
        None

    Returns:
        tuple[int, int]: A tuple of the score for the team and the score against the team.
    """

    score_for = random.randint(0, 6) * 7 + random.randint(0, 3) * 3
    # god mode
    # score_for += 1000000000
    score_against = random.randint(0, 6) * 7 + random.randint(0, 3) * 3
    return score_for, score_against

def start_game(team: Team) -> tuple[str, bool]:
    """
    Starts a game and returns the score and result.

    Args:
        team: Team: The team playing the game.

    Returns:
        tuple[str, bool]: A tuple of the score and result.
    """

    # generate scores
    score_for, score_against = score()

    # tie check
    tie_chance = random.randint(0, 100)
    if score_for == score_against:
        if tie_chance == 1:
            team.add_tie()
            return f"[bold yellow]{score_for:>2}-{score_against:<2}[/bold yellow]", False
        score_for += 3

    # win/loss check
    if score_for > score_against:
        team.add_win()
        return f"[bold green]{score_for:>2}[/bold green]-{score_against:<2}", True

    team.add_loss()
    return f"[bold red]{score_for:>2}[/bold red]-{score_against:<2}", False

def tieless_game(team: Team) -> tuple[str, bool]:
    """
    Starts a game and returns the score and result, but does not count ties.

    Args:
        team: Team: The team playing the game.

    Returns:
        tuple[str, bool]: A tuple of the score and result.
    """

    score_for, score_against = score()

    # tie check
    if score_for == score_against:
        score_for += 3

    # win/loss check
    if score_for > score_against:
        team.add_win()
        return f"[bold green]{score_for:>2}[/bold green]-{score_against:<2}", True

    team.add_loss()
    return f"[bold red]{score_for:>2}[/bold red]-{score_against:<2}", False
