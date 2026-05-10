from rich import print
from core.season import season
from core.team import Team
from rich.console import Console
from rich.align import Align
from rich.panel import Panel
import random

teams = ["Hawks", "Cows", "Dragons", "Wolves"]
cities = ["Atlanta", "Chicago", "Los Angeles", "New York"]

def main():
   console = Console()
   console.clear()

   # Game start/initialization
   console.print(Align.center(Panel.fit("[red]Terminal Football League[/red]", padding=1), vertical="middle"))
   year = int(input("YEAR: "))

   # Career simulation
   team = Team(random.choice(teams), random.choice(cities), year)
   while True:
      season(team)
      team.add_year()
      cont = input("enter to continue: ")
      if cont != "":
         break

if __name__ == "__main__":
   main()