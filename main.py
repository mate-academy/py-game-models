import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        players = json.load(f)

    for key, player in players.items():
        nickname = key
        email = player.get("email")
        bio = player.get("bio")
        race, _ = Race.objects.get_or_create(
            name=player.get("race").get("name"),
            defaults={"description": player.get("race").get("description")},
        )
        for skill in player.get("race").get("skills"):
            Skill.objects.get_or_create(
                name=skill.get("name"),
                bonus=skill.get("bonus"),
                race=race,
            )
        guild = None
        if player.get("guild"):
            guild, _ = Guild.objects.get_or_create(
                name=player.get("guild").get("name"),
                defaults={
                    "description": player.get("guild").get("description")
                },
            )
        Player.objects.get_or_create(
            nickname=nickname,
            defaults={"email": email, "bio": bio, "race": race, "guild": guild}
        )


if __name__ == "__main__":
    main()
