import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    Race.objects.all().delete()
    Skill.objects.all().delete()
    Player.objects.all().delete()
    Guild.objects.all().delete()
    with open("players.json", "r") as players_file:
        players = json.load(players_file)
    for player_name, other in players.items():
        need_add_skill = other.get("race", {}).get("skills", None)
        race = Race.objects.get_or_create(
            name=other.get("race", {}).get("name", None),
            description=other.get("race", {}).get("description", None))
        for skill in need_add_skill:
            Skill.objects.get_or_create(
                name=skill.get("name", None),
                bonus=skill.get("bonus", None),
                race_id=race[0].id
            )
        Player.objects.create(
            nickname=player_name,
            email=other.get("email", None),
            bio=other.get("bio", None),
            race=race[0],
            guild=Guild.objects.get_or_create(
                name=other.get("guild", {}).get("name", None),
                description=other.get("guild", {}).get("description", None)
            )[0] if other.get("guild", None) is not None else None
        )


if __name__ == "__main__":
    main()
