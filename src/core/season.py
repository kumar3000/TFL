from . import game
from rich.table import Table
from rich.console import Console
from rich.progress import track
from rich.live import Live
from rich.align import Align
from .team import Team
import random
import time

# career table initialization
career_table = Table(title="0 Seasons", show_header=True, show_footer=True, header_style="bold magenta", footer_style="bold green")
career_table.add_column("Year", justify="center", footer="0")
career_table.add_column("Record", justify="left", footer="0-0")
career_table_centered = Align.center(career_table)

console = Console()

def create_season_table(team: Team, bye: int) -> Table:
    table = Table(title=f"{team.get_name()} {team.get_year()} Season", show_header=True, header_style="bold magenta")
    table.add_column("WEEK", justify="center")
    table.add_column("BOX SCORE", justify="center")
    table.add_column("RECORD", justify="center")
    table.caption = f"BYE WEEK: {bye + 1}"
    return table

def update_career_table(team: Team, finish: str):
    # career table update
    career_table.title = f"{team.get_seasons() + 1} Seasons" if team.get_seasons() > 0 else "1 Season"
    career_table.footer_style = "bold green" if team.get_wins() > team.get_losses() else "bold red"
    career_table.columns[0].footer = f"{team.get_year()}"
    career_table.columns[1].footer = f"{team.get_record()} {finish}"
    console.print(career_table_centered)
    career_table.add_row(str(team.get_year()), f"{team.get_record()} {finish}")

def regular_season(team: Team, bye: int, season_table: Table):
    for i in range(17) if team.get_year() < 2021 else range(18):
        time.sleep(0.1)
        season_table.add_row(
            f"WEEK {i + 1:<2}" if i != bye else f"[grey35]WEEK {i + 1:<2}[/grey35]",
            game.start_game(team)[0] if bye != i else "[grey35]BYE[/grey35]",
            team.get_record() if bye != i else f"[grey35]{team.get_record()}[/grey35]"
        )

def post_season(team: Team, season_table: Table) -> str:
    # pause after regular season finishes
    time.sleep(2)
    weeks = ["WC", "DIV", "CONF", "SB"]

    # determine bye
    if team.get_losses() < 4:
        weeks.pop(0)
        season_table.add_row(
            f"[grey35]WILDCARD[/grey35]",
            f"[grey35]BYE[/grey35]",
            f"[grey35]{team.get_record()}[/grey35]"
        )

    for week in weeks:
        # post season week
        time.sleep(0.5)
        score, result = game.tieless_game(team)
        season_table.add_row(
            week,
            score,
            team.get_record()
        )

        # break if team loses
        if not result:
            time.sleep(0.5)
            return f"[dodger_blue3]{week} LOSS[/dodger_blue3]"
    
    return f"[gold3]CHAMPION[/gold3]"

def season(team: Team):
    bye = random.randint(5, 12)

    # season table initialization
    season_table = create_season_table(team, bye)
    table_centered = Align.center(season_table)
    console.clear()
    
    # weeks loop
    finish = ""
    with Live(table_centered, refresh_per_second=10):
        regular_season(team, bye, season_table)
        if team.get_losses() < 8:
            finish = post_season(team, season_table)
            
    # update career table
    update_career_table(team, finish)

    # reset team stats
    team.wins = 0
    team.losses = 0
    team.ties = 0