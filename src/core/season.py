from . import game
from rich.table import Table
from rich.console import Console
from .team import Team

def season(team: Team):
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("WEEK", justify="center")
    table.add_column("BOX SCORE", justify="center")
    table.add_column("TEAM", justify="center")
    for i in range(17):
        table.add_row(
            f"WEEK {i+1}",
            game.start_game(team),
            team.get_record()
        )
        console = Console()
        console.print(table, end="\r")
        input()

    # reset team stats
    team.wins = 0
    team.losses = 0
    team.ties = 0