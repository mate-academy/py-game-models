import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as source_file:
        players_data = json.load(source_file)

    for player in players_data:
        guild_ = None
        player_guild = players_data[player]["guild"]
        if player_guild:
            if not Guild.objects.filter(name=player_guild["name"]).exists():
                guild_ = Guild(
                    name=player_guild["name"],
                    description=player_guild["description"],
                )
                guild_.save()
            else:
                guild_ = Guild.objects.filter(name=player_guild["name"])[0]

        race_ = None
        player_race = players_data[player]["race"]
        if player_race:
            if not Race.objects.filter(name=player_race["name"]).exists():
                race_ = Race(
                    name=player_race["name"],
                    description=player_race["description"],
                )
                race_.save()

                skills = player_race["skills"]
                for skill in skills:
                    skill_for_table = Skill(
                        name=skill["name"],
                        bonus=skill["bonus"],
                        race=race_,
                    )
                    skill_for_table.save()
            else:
                race_ = Race.objects.filter(name=player_race["name"])[0]

        player_for_table = Player(
            nickname=player,
            email=players_data[player]["email"],
            bio=players_data[player]["bio"],
            race=race_,
            guild=guild_,
        )
        player_for_table.save()


if __name__ == "__main__":
    main()
