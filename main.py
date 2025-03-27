import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for player_name, player_info in players.items():
        race = player_info.get("race")
        guild = player_info.get("guild")
        skills = race.get("skills")

        Race.objects.get_or_create(
            name=race["name"],
            description=race["description"]
        )
        race = Race.objects.get(name=race["name"])

        for skill in skills:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race_id=race.id
            )

        if guild:
            Guild.objects.get_or_create(
                name=guild["name"],
                description=guild["description"]
            )
        guild = Guild.objects.get(name=guild["name"]) if guild else None

        Player.objects.get_or_create(
            nickname=player_name,
            email=player_info["email"],
            bio=player_info["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
