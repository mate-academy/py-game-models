class Skills:
    def __init__(self, name: str, bonus: str, race: callable) -> None:
        self.name = name
        self.bonus = bonus
        self.race = race
