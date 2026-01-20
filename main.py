import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "rb") as file:
        players = json.load(file)

    for nickname in players:
        if Player.objects.filter(nickname=nickname).exists():
            continue

        player = players[f"{nickname}"]

        if not player.get("race"):
            raise ValueError("Field 'Raise' can't be empty")

        race_data = player["race"]
        race_name = race_data.get("name")
        race_description = race_data.get("description")
        skills = race_data.get("skills")

        race, _ = Race.objects.get_or_create(
            name=race_name,
            description=race_description
        )

        if skills:
            for skill in skills:
                name = skill.get("name")
                bonus = skill.get("bonus")

                Skill.objects.get_or_create(
                    name=name,
                    bonus=bonus,
                    race=race
                )

        guild = player.get("guild")

        if guild:
            guild_name = guild.get("name")
            description = guild.get("description")

            guild, _ = Guild.objects.get_or_create(
                name=guild_name,
                description=description
            )

        else:
            print(guild)
            guild = None

        Player.objects.create(
            nickname=nickname,
            email=player["email"],
            bio=player["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
