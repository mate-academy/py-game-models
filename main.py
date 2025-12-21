import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for nickname, player_data in data.items():

        race_data = player_data["race"]
        race = Race.objects.create(
            name=race_data["name"],
            description=race_data["description"],
        )

        for skill_data in race_data["skills"]:
            Skill.objects.create(
                name=skill_data["name"],
                bonus=skill_data["bonus"],
            )

        guild_data = player_data["guild"]
        guild = None
        if  guild_data:
            guild = Guild.objects.create(
                name=guild_data["name"],
                description=guild_data["description"],
            )

        Player.objects.create(
            nickname=nickname,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
