import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main():
    with open("players.json", "r") as players_file:
        players = json.load(players_file)
        for name in players:

            # Crete races
            race_obj = Race.objects.get_or_create(
                name=players[name]["race"]["name"],
                description=players[name]["race"]["description"])[0]

            # Create skills
            for skill in players[name]["race"]["skills"]:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race_obj
                )

            # Create guilds
            if players[name]["guild"]:
                _description = None

                if players[name]["guild"]["description"]:
                    _description = players[name]["guild"]["description"]

                guild_obj = Guild.objects.get_or_create(
                    name=players[name]["guild"]["name"],
                    description=_description
                )[0]

                # Create players
                Player.objects.get_or_create(
                    nickname=name,
                    email=players[name]["email"],
                    bio=players[name]["bio"],
                    race=race_obj,
                    guild=guild_obj
                )
            else:
                Player.objects.get_or_create(
                    nickname=name,
                    email=players[name]["email"],
                    bio=players[name]["bio"],
                    race=race_obj,
                )


if __name__ == "__main__":
    main()
