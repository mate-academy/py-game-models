import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        players = json.load(f)

    for key, player in players.items():
        nickname = key
        email = player["email"]
        bio = player["bio"]
        race, _ = Race.objects.get_or_create(
            name=player["race"]["name"],
            defaults={"description": player["race"]["description"]},
        )
        for skill in player["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race,
            )
        guild = None
        if player["guild"] is not None:
            guild, _ = Guild.objects.get_or_create(
                name=player["guild"]["name"],
                defaults={"description": player["guild"]["description"]},
            )
        Player.objects.get_or_create(
            nickname=nickname,
            defaults={"email": email, "bio": bio, "race": race, "guild": guild}
        )


if __name__ == "__main__":
    main()
