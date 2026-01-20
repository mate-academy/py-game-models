import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r+") as file:
        players = json.load(file)

    for player, data in players.items():
        race, _ = Race.objects.get_or_create(
            name=data["race"]["name"],
            defaults={"description": data["race"]["description"]}
        )
        for skill in data["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                defaults={"bonus": skill["bonus"], "race": race}
            )

        guild = None
        if data["guild"]:
            guild, _ = Guild.objects.get_or_create(
                name=data["guild"]["name"],
                defaults={"description": data["guild"]["description"]}
            )

        Player.objects.get_or_create(
            nickname=player,
            defaults={
                "email": data["email"],
                "bio": data["bio"],
                "race": race,
                "guild": guild
            }
        )


if __name__ == "__main__":
    main()
