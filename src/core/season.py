from . import game
from rich.table import Table
from rich.console import Console
from .team import Team
import random

def season(team: Team):
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("WEEK", justify="center")
    table.add_column("BOX SCORE", justify="center")
    table.add_column("RECORD", justify="center")
    bye = random.randint(5, 12)
    for i in range(18):
        table.add_row(
            f"WEEK {i + 1}",
            game.start_game(team) if bye != i else "BYE",
            team.get_record()
        )
        console = Console()
        console.clear()
        console.print(table)
        input()

    # reset team stats
    team.wins = 0
    team.losses = 0
    team.ties = 0