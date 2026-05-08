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

    def get_name(self) -> str:
        return f"{self.city} {self.name}"

    def get_record(self) -> str:
        if self.ties > 0:
            return f"{self.wins}-{self.losses}-{self.ties}"
        else:
            return f"{self.wins}-{self.losses}"