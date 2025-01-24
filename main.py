import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:

    with open("players.json", "r") as file:
        player_data = json.load(file)

    for nickname, data in player_data.items():
        race, created_race = Race.objects.get_or_create(
            name=data["race"]["name"],
            description=data["race"]["description"],
        )

        for skills_data in data["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skills_data["name"],
                bonus=skills_data["bonus"],
                race=race,
            )

        if data["guild"]:
            guild, created_guild = Guild.objects.get_or_create(
                name=data["guild"]["name"],
                description=data["guild"].get("description", "")
            )
        else:
            guild = None

        player, created = Player.objects.get_or_create(
            nickname=nickname,
            email=data.get("email"),
            bio=data.get("bio"),
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
