from rich import print
from core.season import season
from core.team import Team
from rich.console import Console

def main():
   console = Console()
   console.clear()
   print("[bold red]Terminal Football League[/bold red]")
   city = input("Enter your team city: ")
   name = input("Enter your team name: ")
   team = Team(name, city)
   season(team)

if __name__ == "__main__":
    main()