import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    Race.objects.all().delete()
    Skill.objects.all().delete()
    Guild.objects.all().delete()
    Player.objects.all().delete()

    with open("players.json") as file:
        players = json.load(file)

    for player, values in players.items():
        nickname, email, bio, race = (
            player,
            values["email"],
            values["bio"],
            values["race"],
        )

        race_name, race_description = race["name"], race["description"]

        if Race.objects.filter(name=race_name).exists():
            pass
        else:
            race_obj = Race.objects.create(
                name=race_name, description=race_description
            )

        skills = race["skills"]
        for skill in skills:
            name = skill["name"]
            bonus = skill["bonus"]
            if Skill.objects.filter(name=name).exists():
                pass
            else:
                Skill.objects.create(name=name, bonus=bonus, race=race_obj)

        guild = values.get("guild")
        guild_obj = None
        if guild:
            guild_name = guild["name"]
            guild_description = guild["description"]
            if Guild.objects.filter(name=guild_name).exists():
                guild_obj = Guild.objects.get(name=guild_name)
            else:
                guild_obj = Guild.objects.create(
                    name=guild_name, description=guild_description
                )

        Player.objects.create(
            nickname=nickname,
            email=email,
            bio=bio,
            race=race_obj,
            guild=guild_obj if guild else None,
        )


if __name__ == "__main__":
    main()
