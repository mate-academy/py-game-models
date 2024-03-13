import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    Race.objects.delete()
    Skill.objects.delete()
    Guild.objects.delete()
    Player.objects.delete()

    with open("players.json") as f:
        players = json.load(f)

    for player in players:
        race_name = players[player]["race"]["name"]
        race_description = players[player]["race"]["description"]
        race, _ = Race.objects.get_or_create(
            name=race_name,
            description=race_description
        )

        for skill in players[player]["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race_id=race.id
            )

        if guild_data := players[player]["guild"]:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                description=guild_data["description"]
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
