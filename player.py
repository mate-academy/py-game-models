class Player:
    def __init__(self,
                 nickname: str,
                 email: str,
                 bio: str,
                 race: callable,
                 guild: callable) -> None:
        self.nickname = nickname
        self.email = email
        self.bio = bio
        self.race = race
        self.guild = guild
