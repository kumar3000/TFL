from . import game
from rich.table import Table
from rich.console import Console
from rich.progress import track
from rich.live import Live
from rich.align import Align
from .team import Team
import random
import time

def season(team: Team):
    bye = random.randint(5, 12)

    table = Table(title=f"{team.get_name()} YEAR Season", show_header=True, header_style="bold magenta")
    table_centered = Align.center(table)
    table.add_column("WEEK", justify="center")
    table.add_column("BOX SCORE", justify="center")
    table.add_column("RECORD", justify="center")
    table.caption = f"BYE WEEK: {bye + 1}"
    console = Console()
    console.clear()
    with Live(table_centered, refresh_per_second=10):
        for i in range(18):
            time.sleep(0.4)
            table.add_row(
                f"WEEK {i + 1:<2}" if i != bye else f"[grey35]WEEK {i + 1:<2}[/grey35]",
                game.start_game(team) if bye != i else "[grey35]BYE[/grey35]",
                team.get_record() if bye != i else f"[grey35]{team.get_record()}[/grey35]"
            )

    # reset team stats
    team.wins = 0
    team.losses = 0
    team.ties = 0