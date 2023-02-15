from db.models import Race, Skill, Player, Guild


class CreateBase:

    @staticmethod
    def create_race(
            name: str,
            description: str = "",
            model: Race = Race,
    ) -> Race:
        is_race_exists = model.objects.filter(
            name=name
        ).exists()
        if is_race_exists:
            return model.objects.get(
                name=name
            )
        race_instance = model.objects.create(
            name=name,
            description=description
        )
        return race_instance

    @staticmethod
    def create_skill(
            name: str,
            bonus: str,
            race: Race,
            model: Skill = Skill,
    ) -> Skill:
        is_skill_exists = model.objects.filter(
            name=name
        ).exists()
        if is_skill_exists:
            return model.objects.get(
                name=name
            )
        skill_instance = model.objects.create(
            name=name,
            bonus=bonus,
            race=race,
        )
        return skill_instance

    @staticmethod
    def create_guild(
            name: str,
            description: str = None,
            model: Guild = Guild,
    ) -> Guild:
        is_guild_exists = model.objects.filter(
            name=name
        ).exists()
        if is_guild_exists:
            return model.objects.get(name=name)
        guild_instance = model.objects.create(
            name=name,
            description=description
        )
        return guild_instance

    @staticmethod
    def create_player(
            player_name: str,
            player: dict,
            model: Player = Player,
    ) -> Player:
        is_player_exists = model.objects.filter(
            nickname=player_name
        ).exists()

        if is_player_exists:
            return model.objects.get(
                nickname=player_name
            )

        race = CreateBase.create_race(
            player["race"]["name"],
            player["race"]["description"],
        )

        for skill in player["race"]["skills"]:
            CreateBase.create_skill(
                skill["name"],
                skill["bonus"],
                race=race,
            )

        guild = None
        guild_dict = player["guild"]

        if guild_dict:
            guild = CreateBase.create_guild(
                name=player["guild"]["name"],
                description=player["guild"]["description"],
            )

        player_instance = Player.objects.create(
            nickname=player_name,
            email=player["email"],
            bio=player["bio"],
            race=race,
            guild=guild
        )
        return player_instance
