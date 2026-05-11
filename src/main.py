"""
This module is the main module for the Terminal Football League.

Functions:
    main(): Runs the main season loop.
"""

import random
from rich.console import Console
from rich.align import Align
from rich.panel import Panel
from core.season import season
from core.team import Team

teams = {
    "Atlanta": "Falcons",
    "Arizona": "Cardinals",
    "Baltimore": "Ravens",
    "Buffalo": "Bills",
    "Carolina": "Panthers",
    "Chicago": "Bears",
    "Cincinnati": "Bengals",
    "Cleveland": "Browns",
    "Dallas": "Cowboys",
    "Denver": "Broncos",
    "Detroit": "Lions",
    "Green Bay": "Packers",
    "Houston": "Texans",
    "Indianapolis": "Colts",
    "Jacksonville": "Jaguars",
    "Kansas City": "Chiefs",
    "Las Vegas": "Raiders",
    "Los Angeles N": "Rams",
    "Los Angeles A": "Chargers",
    "Miami": "Dolphins",
    "Minnesota": "Vikings",
    "New England": "Patriots",
    "New Orleans": "Saints",
    "New York N": "Giants",
    "New York A": "Jets",
    "Philadelphia": "Eagles",
    "Pittsburgh": "Steelers",
    "San Francisco": "49ers",
    "Seattle": "Seahawks",
    "Tampa Bay": "Buccaneers",
    "Tennessee": "Titans",
    "Washington": "Football Team"
}

console = Console()
console.clear()

def main():
    """
    Runs the main season loop.
    """

    # Game start/initialization
    console.print(
        Align.center(Panel.fit("[red]Terminal Football League[/red]", padding=1),
        vertical="middle"))
    year = int(input("YEAR: "))

    # Career simulation
    city, name = random.choice(list(teams.items()))
    team = Team(name, city, year)
    while True:
        season(team)
        team.add_year()
        if team.get_seasons() == 20:
            console.print(
                Align.center(Panel.fit(
                    "[gold3]You retire a veteran and a legend![/gold3]",
                    padding=1),
                vertical="middle"))
            break
        cont = input("enter to continue: ")
        if cont != "":
            break

if __name__ == "__main__":
    main()
