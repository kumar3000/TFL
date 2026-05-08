class Team:
    name: str
    city: str
    wins: int
    losses: int
    ties: int

    def __init__(self, name: str, city: str):
        self.name = name
        self.city = city
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

    def get_record(self) -> str:
        if self.ties > 0:
            return f"{self.wins}-{self.losses}-{self.ties}"
        else:
            return f"{self.wins}-{self.losses}"