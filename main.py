import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players = json.load(file)

    for player_name, player_info in players.items():
        new_race, _ = Race.objects.get_or_create(
            name=player_info["race"].get("name"),
            description=player_info["race"].get("description"),
        )
        for skill in player_info["race"]["skills"]:
            if not Skill.objects.filter(name=skill.get("name")).exists():
                Skill.objects.create(
                    name=skill.get("name"), bonus=skill.get("bonus"), race=new_race
                )
        if player_info["guild"] is not None:
            new_guild, _ = Guild.objects.get_or_create(
                name=player_info["guild"].get("name"),
                description=player_info["guild"].get("description"),
            )
        else:
            new_guild = None

        if not Player.objects.filter(nickname=player_name).exists():
            Player.objects.create(
                nickname=player_name,
                email=player_info.get("email"),
                bio=player_info.get("bio"),
                race=new_race,
                guild=new_guild,
            )


if __name__ == "__main__":
    main()
