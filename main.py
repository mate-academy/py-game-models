import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    Race.objects.all().delete()
    Skill.objects.all().delete()
    Guild.objects.all().delete()
    Player.objects.all().delete()

    with open("players.json") as f:
        players = json.load(f)
        for player in players:
            race_name = players[player]["race"]["name"]
            race_description = players[player]["race"]["description"]
            race, create = Race.objects.get_or_create(
                name=race_name,
                description=race_description
            )

            for skill in players[player]["race"]["skills"]:
                name = skill["name"]
                bonus = skill["bonus"]
                Skill.objects.get_or_create(
                    name=name,
                    bonus=bonus,
                    race_id=race.id
                )

            if players[player]["guild"] is not None:
                guild_name = players[player]["guild"]["name"]
                guild_description = players[player]["guild"]["description"]
                guild, create = Guild.objects.get_or_create(
                    name=guild_name,
                    description=guild_description
                )
                guild_id = guild.id
            else:
                guild_id = None

            nickname = player
            email = players[player]["email"]
            bio = players[player]["bio"]
            Player.objects.get_or_create(
                nickname=nickname,
                email=email,
                bio=bio,
                race_id=race.id,
                guild_id=guild_id
            )


if __name__ == "__main__":
    main()
