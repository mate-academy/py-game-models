import json

from db.models import Guild, Player, Race, Skill
import init_django_orm  # noqa: F401


def main() -> None:
    with open("players.json", "r") as f:
        players_data = json.load(f)

    for nickname, data in players_data.items():
        race, _ = Race.objects.get_or_create(
            name=data["race"]["name"],
            defaults={"description": data["race"]["description"]}
        )

        for skill in data["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )

        if data["guild"]:
            guild, _ = Guild.objects.get_or_create(
                name=data["guild"]["name"],
                defaults={"description": data["guild"]["description"]}
            )
        else:
            guild = None

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": data["email"],
                "bio": data["bio"],
                "race": race,
                "guild": guild
            }
        )


if __name__ == "__main__":
    main()
