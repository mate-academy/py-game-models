from json import load

import init_django_orm  # noqa: F401
from db.models import Race, Skill, Guild, Player


def main():
    with open("players.json") as f:
        players = load(f)

    for player, settings in players.items():
        character = players[player]
        if character["race"]:
            # Create Race
            try:
                race = Race.objects.get(name=character["race"]["name"])
            except Race.DoesNotExist:
                race = Race.objects.create(
                    name=character["race"]["name"],
                    description=character["race"]["description"])

            # Create Skills
            for skill in character["race"]["skills"]:
                skill_name, skill_bonus = skill.values()
                try:
                    Skill.objects.get(name=skill["name"])
                except Skill.DoesNotExist:
                    Skill.objects.create(name=skill_name, bonus=skill_bonus,
                                         race=race)

            # Create Guild
            try:
                guild = Guild.objects.get(name=character["guild"]["name"])
            except Guild.DoesNotExist:
                guild_name, guild_description = character["guild"].values()
                guild = Guild.objects.create(name=guild_name,
                                             description=guild_description)
            except TypeError:
                guild = None

        # Create Player
        try:
            Player.objects.get(nickname=player)
        except Player.DoesNotExist:
            Player.objects.create(nickname=player, email=character["email"],
                                  bio=character["bio"], race=race, guild=guild)


if __name__ == "__main__":
    main()
