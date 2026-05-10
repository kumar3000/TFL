class Team:
    name: str
    city: str
    wins: int
    losses: int
    ties: int
    year: int
    seasons: int

    def __init__(self, name: str, city: str, year: int):
        self.name = name
        self.city = city
        self.year = year
        self.seasons = 0
        self.wins = 0
        self.losses = 0
        self.ties = 0

    def add_win(self):
        self.wins += 1
    
    def add_loss(self):
        self.losses += 1
    
    def add_tie(self):
        self.ties += 1

    def get_name(self) -> str:
        return f"{self.city} {self.name}"

    def get_year(self) -> int:
        return self.year

    def get_seasons(self) -> int:
        return self.seasons
    
    def add_year(self):
        self.year += 1
        self.seasons += 1

    def get_record(self) -> str:
        if self.ties > 0:
            return f"{self.wins}-{self.losses}-{self.ties}"
        else:
            return f"{self.wins}-{self.losses}"