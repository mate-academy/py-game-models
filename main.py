import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players:
        players = json.load(players)
    for key in players:
        player_guild_dict = players[key]["guild"]
        if player_guild_dict:
            guild, _ = (Guild.objects.get_or_create(
                name=player_guild_dict["name"],
                description=player_guild_dict["description"])
            )
        else:
            guild = None
        skills_to_add = []
        race, _ = Race.objects.get_or_create(
            name=players[key]["race"]["name"],
            description=players[key]["race"]["description"]
        )

        for skill in players[key]["race"]["skills"]:
            skills_to_add.append((Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"], race=race))[0])

        Player.objects.get_or_create(
            nickname=key,
            email=players[key]["email"],
            bio=players[key]["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
