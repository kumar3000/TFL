"""
This module handles the season simulation.

Functions:
    create_season_table(team: Team, bye: int) -> Table: Creates a season table.
    update_career_table(team: Team, finish: str): Updates the career table.
    regular_season(team: Team, bye: int, season_table: Table, centered: Align): Centered table.
    post_season(team: Team, season_table: Table, centered: Align) -> str: Runs the post season.
    season(team: Team): Runs the season.
"""

import random
from rich.table import Table
from rich.console import Console
from rich.align import Align
from .team import Team
from . import game

# career table initialization
career_table = Table(
    title="0 Seasons",
    show_header=True,
    show_footer=True,
    header_style="bold magenta",
    footer_style="bold green")
career_table.add_column("Year", justify="center", footer="0")
career_table.add_column("Record", justify="left", footer="0-0")
career_table_centered = Align.center(career_table)

console = Console()

def create_season_table(team: Team, bye: int) -> Table:
    """
    Creates a season table.

    Args:
        team: Team: The team to create the season table for.
        bye: int: The bye week.

    Returns:
        Table: The season table.
    """

    table = Table(
        title=f"{team.get_name()} {team.get_year()} Season",
        show_header=True,
        header_style="bold magenta")
    table.add_column("WEEK", justify="center")
    table.add_column("BOX SCORE", justify="center")
    table.add_column("RECORD", justify="center")
    table.caption = f"BYE WEEK: {bye + 1}"
    return table

def update_career_table(team: Team, finish: str):
    """
    Updates the career table.

    Args:
        team: Team: The team to update the career table for.
        finish: str: The result of the season.
    """

    # career table update
    if team.get_seasons() > 0:
        career_table.title = f"{team.get_seasons() + 1} Seasons"
    else:
        career_table.title = "1 Season"

    if team.get_wins() > team.get_losses():
        career_table.footer_style = "bold green"
    else:
        career_table.footer_style = "bold red"

    career_table.columns[0].footer = f"{team.get_year()}"
    career_table.columns[1].footer = f"{team.get_record():<6} {finish}"
    console.print(career_table_centered)
    career_table.add_row(str(team.get_year()), f"{team.get_record():<6} {finish}")

def regular_season(team: Team, bye: int, season_table: Table, centered: Align):
    """
    Runs the regular season.

    Args:
        team: Team: The team to run the regular season for.
        bye: int: The bye week.
        season_table: Table: The season table.
        centered: Align: The centered alignment.
    """

    for i in range(17) if team.get_year() < 2021 else range(18):
        season_table.add_row(
            f"WEEK {i + 1:<2}" if i != bye else f"[grey35]WEEK {i + 1:<2}[/grey35]",
            game.start_game(team)[0] if bye != i else "[grey35]BYE[/grey35]",
            team.get_record() if bye != i else f"[grey35]{team.get_record()}[/grey35]"
        )
        console.clear()
        console.print(centered)
        input()

def post_season(team: Team, season_table: Table, centered: Align) -> str:
    """
    Runs the post season.

    Args:
        team: Team: The team to run the post season for.
        season_table: Table: The season table.
        centered: Align: The centered alignment.

    Returns:
        str: The result of the post season.
    """

    weeks = ["WC", "DIV", "CONF", "SB"]

    # determine bye
    if team.get_losses() < 4:
        weeks.pop(0)
        season_table.add_row(
            "[grey35]WILDCARD[/grey35]",
            "[grey35]BYE[/grey35]",
            f"[grey35]{team.get_record()}[/grey35]"
        )

    for week in weeks:
        # post season week
        score, result = game.tieless_game(team)
        season_table.add_row(
            week,
            score,
            team.get_record()
        )
        console.clear()
        console.print(centered)
        input()

        # return result if team loses
        if not result:
            if week == "SB":
                return f"[bold red]{week} LOSS[/bold red]"
            return f"[dodger_blue3]{week} LOSS[/dodger_blue3]"

    return "[gold3]CHAMPION[/gold3]"

def season(team: Team):
    """
    Runs the season.

    Args:
        team: Team: The team to run the season for.
    """

    bye = random.randint(5, 12)

    # season table initialization
    season_table = create_season_table(team, bye)
    table_centered = Align.center(season_table)
    console.clear()

    # weeks loop
    finish = ""
    regular_season(team, bye, season_table, table_centered)
    if team.get_losses() < 8:
        finish = post_season(team, season_table, table_centered)

    # update career table
    update_career_table(team, finish)

    # reset team stats
    team.wins = 0
    team.losses = 0
    team.ties = 0
