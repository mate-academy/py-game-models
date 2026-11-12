import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
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

        race_obj, _ = Race.objects.get_or_create(
            name=race_name, description=race_description
        )

        skills = race["skills"]
        for skill in skills:
            name = skill["name"]
            bonus = skill["bonus"]

            Skill.objects.get_or_create(name=name, bonus=bonus, race=race_obj)

        guild_obj = None

        if guild := values.get("guild"):
            guild_name = guild["name"]
            guild_description = guild["description"]

            guild_obj, _ = Guild.objects.get_or_create(
                name=guild_name, description=guild_description
            )

        if not Player.objects.filter(nickname=nickname).exists():
            Player.objects.create(
                nickname=nickname,
                email=email,
                bio=bio,
                race=race_obj,
                guild=guild_obj,
            )
        else:
            print(f"User with nickname '{nickname}' already exists!")


if __name__ == "__main__":
    main()
