import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with (open('players.json', "r")) as players_file:
        players = json.load(players_file)

    for nickname, player in players.items():
        guild = player["guild"]
        race = player["race"]
        guild_id = None
        race_id = None

        if guild:
            guild_db = Guild.objects.get_or_create(
                name = guild["name"], description=guild["description"]
            )
            guild_id = guild_db[0].id

        if race:
            race_db = Race.objects.get_or_create(
                name = race["name"], description=race["description"]
            )
            race_id = race_db[0].id

            if len(race["skills"]) > 0:
                for skill in race["skills"]:
                    Skill.objects.get_or_create(
                        name=skill["name"], bonus=skill["bonus"],
                        race_id=race_id)

        Player.objects.get_or_create(nickname=nickname,
                                     email=player["email"], bio=player["bio"],
                                     race_id=race_id, guild_id=guild_id)




if __name__ == "__main__":
    main()
