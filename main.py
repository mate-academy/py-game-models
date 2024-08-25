import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild
import json


def main() -> None:
    with open("players.json") as f:
        players_data = json.load(f)

    for player in players_data:

        race_description = players_data[player]["race"]["description"]
        race_obj, _ = Race.objects.get_or_create(
            name=players_data[player]["race"]["name"],
            description=race_description
            if race_description is not None
            else ""
        )

        for skill in players_data[player]["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                race=race_obj,
                bonus=skill["bonus"],
            )

        if players_data[player]["guild"]:
            guild_name = players_data[player]["guild"]["name"]
            guild_description = players_data[player]["guild"]["description"]
            guild_obj, _ = Guild.objects.get_or_create(
                name=guild_name,
                description=guild_description
            )
        else:
            guild_obj = None

        Player.objects.update_or_create(
            nickname=player,
            defaults={
                "email": players_data[player]["email"],
                "bio": players_data[player]["bio"],
                "race": race_obj,
                "guild": guild_obj,
            }
        )


if __name__ == "__main__":
    main()
