import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players = json.load(file)

    for player_name, player_info in players.items():
        if not Race.objects.filter(name=player_info["race"]["name"]).exists():
            Race.objects.create(
                name=player_info["race"]["name"],
                description=player_info["race"]["description"],
            )
            new_race = Race.objects.filter(
                name=player_info["race"]["name"]
            ).get()
            for skill in player_info["race"]["skills"]:
                if not Skill.objects.filter(name=skill["name"]).exists():
                    Skill.objects.create(
                        name=skill["name"], bonus=skill["bonus"], race=new_race
                    )
        else:
            new_race = Race.objects.filter(
                name=player_info["race"]["name"]
            ).get()

        if player_info["guild"] is None:
            new_guild = None
        elif not Guild.objects.filter(
                name=player_info["guild"]["name"]
        ).exists():
            Guild.objects.create(
                name=player_info["guild"]["name"],
                description=player_info["guild"]["description"],
            )
            new_guild = Guild.objects.filter(
                name=player_info["guild"]["name"]
            ).get()
        else:
            new_guild = Guild.objects.filter(
                name=player_info["guild"]["name"]
            ).get()

        if not Player.objects.filter(nickname=player_name).exists():
            Player.objects.create(
                nickname=player_name,
                email=player_info["email"],
                bio=player_info["bio"],
                race=new_race,
                guild=new_guild,
            )


if __name__ == "__main__":
    main()
