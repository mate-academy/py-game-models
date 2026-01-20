import init_django_orm  # noqa: F401
import json


from db.models import Race, Skill, Player, Guild


def create_players(filename: str) -> None:
    with open(filename, "r") as file_in:
        players_data = json.load(file_in)
        for player_name, player_data in players_data.items():

            race, created_race = Race.objects.get_or_create(
                name=player_data["race"]["name"],
                description=player_data["race"]["description"]
            )
            if player_data["guild"] is not None:
                guild, created_guild = Guild.objects.get_or_create(
                    name=player_data["guild"]["name"],
                    description=player_data["guild"]["description"]
                )
            else:
                guild = None

            Player.objects.create(
                nickname=player_name,
                email=player_data["email"],
                bio=player_data["bio"],
                race=race,
                guild=guild
            )

            for skill in player_data["race"]["skills"]:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )


def main() -> None:
    create_players("players.json")


if __name__ == "__main__":
    main()
