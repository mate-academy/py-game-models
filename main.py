import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as players_file:
        players = json.load(players_file)
    for nickname, player in players.items():
        race, created = Race.objects.get_or_create(
            name=player["race"]["name"],
            description=player["race"]["description"],
        )
        for skill_data in player["race"]["skills"]:
            skill, created = Skill.objects.get_or_create(
                name=skill_data["name"],
                bonus=skill_data["bonus"],
                race=race,
            )
        if player["guild"]:
            guild_description = player["guild"]["description"] \
                if player["guild"]["description"] else None
            guild, created = Guild.objects.get_or_create(
                name=player["guild"]["name"],
                description=guild_description,
            )
        else:
            guild = None
        new_player, created = Player.objects.get_or_create(
            nickname=nickname,
            email=player["email"],
            bio=player["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
