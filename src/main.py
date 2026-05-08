from rich import print
from core.season import season
from core.team import Team
from rich.console import Console
from rich.align import Align
from rich.panel import Panel

def main():
   console = Console()
   console.clear()
   console.print(Align.center(Panel.fit("[red]Terminal Football League[/red]", padding=1), vertical="middle"))
   print("CITY: ", end="")
   city = input()
   print("NAME: ", end="")
   name = input()
   team = Team(name, city)
   season(team)

if __name__ == "__main__":
   main()