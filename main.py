import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players:
        data = json.load(players)

    for nickname, abilities in data.items():
        race, _ = Race.objects.get_or_create(
            name=abilities["race"]["name"],
            description=abilities["race"]["description"]
        )
        guild = None
        if guild_ := abilities["guild"]:
            guild, _ = Guild.objects.get_or_create(
                name=guild_["name"],
                description=guild_["description"],
            )
        for skill in abilities["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race,
            )
        Player.objects.get_or_create(
            nickname=nickname,
            email=abilities["email"],
            bio=abilities["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
