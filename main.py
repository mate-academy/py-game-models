import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main():
    with open("players.json", "r") as player_file:
        players = json.load(player_file)

    for nick_name, item in players.items():
        guild = None
        if item["guild"] is not None:
            guild, _ = Guild.objects.get_or_create(**item["guild"])

        race, _ = Race.objects.get_or_create(
            name=item["race"]["name"],
            description=item["race"]["description"]
        )

        if item["race"]["skills"]:
            for skill in item["race"]["skills"]:
                Skill.objects.get_or_create(race=race, **skill)
        Player.objects.create(
            nickname=nick_name,
            email=item["email"],
            bio=item["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
