import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        player_data = json.load(file)

    for nickname, data in player_data.items():
        race_name = data["race"]["name"]
        race_desc = data["race"]["description"]
        race, _ = Race.objects.get_or_create(
            name=race_name,
            description=race_desc
        )

        guild = None
        if data["guild"]:
            guild_name = data["guild"]["name"]
            guild_desc = data["guild"]["description"]
            guild, _ = Guild.objects.get_or_create(
                name=guild_name,
                description=guild_desc
            )

        for skill_data in data["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill_data["name"],
                bonus=skill_data["bonus"],
                race=race
            )

        Player.objects.create(
            nickname=nickname,
            email=data["email"],
            bio=data["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
