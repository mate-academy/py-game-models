import os
import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    players = file_data("players.json")

    # print(players)
    # show_schem(players)

    for player, info in players.items():
        email_info = info.get("email")
        bio_info = info.get("bio")

        if race_info := info.get("race"):
            race_name = race_info.get("name")
            race_description = race_info.get("description")

            race, race_created = Race.objects.get_or_create(
                name=race_name,
                description=race_description
            )

            if skills_info := race_info.get("skills"):
                for skill in skills_info:
                    skill_name = skill.get("name")
                    skill_bonus = skill.get("bonus")

                    skill, skill_created = Skill.objects.get_or_create(
                        name=skill_name, bonus=skill_bonus, race=race
                    )

        if guild_info := info.get("guild"):
            guild_name = guild_info.get("name")
            guild_description = guild_info.get("description")

            guild, guild_created = Guild.objects.get_or_create(
                name=guild_name,
                description=guild_description
            )
        else:
            guild = None

        Player.objects.create(
            nickname=player,
            email=email_info,
            bio=bio_info,
            race=race,
            guild=guild
        )


def file_data(path):
    file_path = os.path.join(path)
    with open(file_path) as f:
        players = json.load(f)

    return players


def show_schem(players):
    for player, info in players.items():
        print(player)
        print("email: ", info.get("email"))
        print("bio: ", info.get("bio"))

        if race_info := info.get("race"):
            print("race")
            print("name:", race_info.get("name"))
            print("description:", race_info.get("description"))

            if skills_info := race_info.get("skills"):
                print("skills")
                for skill in skills_info:
                    print("name:", skill.get("name"))
                    print("bonus:", skill.get("bonus"))

        if guild_info := info.get("guild"):
            print("guild")
            print("name:", guild_info.get("name"))
            print("description:", guild_info.get("description"))

        print("-" * 30)


if __name__ == "__main__":
    main()
