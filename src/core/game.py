import random
from .team import Team

def score() -> int:
    return random.randint(0, 6) * 7 + random.randint(0, 3) * 3

def start_game(team: Team) -> str:
    score_for = score()
    score_against = score()
    if score_for > score_against:
        team.add_win()
        return f"[bold green]{score_for:>2}[/bold green]-{score_against:<2}"
    elif score_for < score_against:
        team.add_loss()
        return f"[bold red]{score_for:>2}[/bold red]-{score_against:<2}"
    else:
        team.add_tie()
        return f"[bold yellow]{score_for:>2}-{score_against:<2}[/bold yellow]"