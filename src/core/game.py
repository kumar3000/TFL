import random
from .team import Team

def score() -> int:
    return random.randint(0, 6) * 7 + random.randint(0, 3) * 3

def start_game(team: Team) -> str:
    score_for = score()
    score_against = score()
    if score_for > score_against:
        team.wins += 1
        return f"[bold green]{score_for}[/bold green]-{score_against} FINAL"
    elif score_for < score_against:
        team.losses += 1
        return f"[bold red]{score_for}[/bold red]-{score_against} FINAL"
    else:
        team.ties += 1
        return f"[bold yellow]{score_for}-{score_against}[/bold yellow] FINAL"