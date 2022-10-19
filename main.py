import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file_open:
        players_file = json.load(file_open)

    for player, fields in players_file.items():
        if not Race.objects.filter(name=fields["race"]["name"]).exists():
            race = Race.objects.create(
                name=fields["race"]["name"],
                description=fields["race"]["description"]
            )
        else:
            race = Race.objects.get(name=fields["race"]["name"])

        for skill in fields["race"]["skills"]:
            if not Skill.objects.filter(name=skill["name"]).exists():
                skill = Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )
            else:
                skill = Skill.objects.get(name=skill["name"])

        if fields["guild"]:
            if not Guild.objects.filter(name=fields["guild"]["name"]).exists():
                guild = Guild.objects.create(
                    name=fields["guild"]["name"],
                    description=fields["guild"]["description"]
                )
            else:
                guild = Guild.objects.get(name=fields["guild"]["name"])
        else:
            guild = None

        if not Player.objects.filter(nickname=player).exists():
            Player.objects.create(
                nickname=player,
                email=fields["email"],
                bio=fields["bio"],
                race=race,
                guild=guild
            )


if __name__ == "__main__":
    main()
