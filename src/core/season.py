from . import game
from rich.table import Table
from rich.console import Console
from rich.progress import track
from rich.live import Live
from rich.align import Align
from .team import Team
import random
import time

career_table = Table(title="Career - Season 0", show_header=True, header_style="bold magenta")
career_table.add_column("Year", justify="center")
career_table.add_column("Record", justify="center")
career_table_centered = Align.center(career_table)

def season(team: Team):
    bye = random.randint(5, 12)

    table = Table(title=f"{team.get_name()} {team.get_year()} Season", show_header=True, header_style="bold magenta")
    table_centered = Align.center(table)
    table.add_column("WEEK", justify="center")
    table.add_column("BOX SCORE", justify="center")
    table.add_column("RECORD", justify="center")
    table.caption = f"BYE WEEK: {bye + 1}"
    console = Console()
    console.clear()
    
    # weeks loop
    with Live(table_centered, refresh_per_second=10):
        for i in range(17) if team.get_year() < 2021 else range(18):
            time.sleep(0.1)
            table.add_row(
                f"WEEK {i + 1:<2}" if i != bye else f"[grey35]WEEK {i + 1:<2}[/grey35]",
                game.start_game(team) if bye != i else "[grey35]BYE[/grey35]",
                team.get_record() if bye != i else f"[grey35]{team.get_record()}[/grey35]"
            )
        career_table.add_row(str(team.get_year()), team.get_record())

    career_table.title = f"{team.get_seasons() + 1} Seasons" if team.get_seasons() > 0 else f"{team.get_seasons() + 1} Season"

    console.print(career_table_centered)

    # reset team stats
    team.wins = 0
    team.losses = 0
    team.ties = 0