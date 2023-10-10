import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open(
            "C:/Users/user/Desktop/py-game-models/players.json", "r"
    ) as players_file:
        players_data = json.load(players_file)

        for player, data in players_data.items():
            data_of_race = data["race"]
            race, bool_value = Race.objects.get_or_create(
                name=data_of_race["name"],
                defaults={"description": data_of_race["description"]}
            )

            for skill_data in data_of_race["skills"]:
                Skill.objects.get_or_create(
                    name=skill_data["name"],
                    defaults={"bonus": skill_data["bonus"], "race": race}
                )

            data_of_guild = data["guild"]
            if data_of_guild is not None:
                guild, bool_value = Guild.objects.get_or_create(
                    name=data_of_guild["name"],
                    defaults={"description": data_of_guild["description"]}
                )
            else:
                guild = None

            Player.objects.get_or_create(
                nickname=player,
                defaults={
                    "email": data["email"],
                    "bio": data["bio"],
                    "race": race,
                    "guild": guild
                }
            )


if __name__ == "__main__":
    main()
