import random
from .team import Team

def score() -> tuple[int, int]:
    score_for = random.randint(0, 6) * 7 + random.randint(0, 3) * 3
    score_against = random.randint(0, 6) * 7 + random.randint(0, 3) * 3
    return score_for, score_against

def start_game(team: Team) -> tuple[str, bool]:
    # generate scores
    score_for, score_against = score()

    # tie check
    tie_chance = random.randint(0, 100)
    if score_for == score_against:
        if tie_chance == 1:
            team.add_tie()
            return f"[bold yellow]{score_for:>2}-{score_against:<2}[/bold yellow]", False
        else:
            score_for += 3

    # win/loss check
    if score_for > score_against:
        team.add_win()
        return f"[bold green]{score_for:>2}[/bold green]-{score_against:<2}", True
    elif score_for < score_against:
        team.add_loss()
        return f"[bold red]{score_for:>2}[/bold red]-{score_against:<2}", False

def tieless_game(team: Team) -> tuple[str, bool]:
    score_for, score_against = score()

    # tie check
    if score_for == score_against:
        score_for += 3

    # win/loss check
    if score_for > score_against:
        team.add_win()
        return f"[bold green]{score_for:>2}[/bold green]-{score_against:<2}", True
    elif score_for < score_against:
        team.add_loss()
        return f"[bold red]{score_for:>2}[/bold red]-{score_against:<2}", False