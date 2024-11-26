import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "rb") as players_file:
        players_dict = json.load(players_file)

    for player_name, player_info in players_dict.items():
        race_name = player_info["race"]["name"]
        race_description = player_info["race"]["description"]
        race = (
            Race.objects.get(name=race_name) if
            Race.objects.filter(name=race_name).exists() else
            Race(
                name=race_name,
                description=race_description
            )
        )
        race.save()

        guild = player_info["guild"]
        if guild is not None:
            guild_name = player_info["guild"]["name"]
            guild = (
                Guild.objects.get(name=guild_name) if
                Guild.objects.filter(name=guild_name).exists() else
                Guild(
                    name=guild_name,
                    description=player_info["guild"]["description"]
                )
            )
            guild.save()

        for skill_dict in player_info["race"]["skills"]:
            if not Skill.objects.filter(name=skill_dict["name"]).exists():
                Skill(
                    name=skill_dict["name"],
                    bonus=skill_dict["bonus"],
                    race=race
                ).save()

        player = Player(
            nickname=player_name,
            email=player_info["email"],
            bio=player_info["bio"],
            race=race,
            guild=guild
        )
        player.save()


if __name__ == "__main__":
    main()
