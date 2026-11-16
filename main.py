import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild

import json


def main() -> None:

    with open("players.json", "r") as file:
        players = json.load(file)
        print(players)
        for player, data in players.items():
            print(data["race"]["name"])
            print(player)
            print(data["email"])
            race_name = data["race"]["name"]
            race_description = data["race"]["description"]
            race, created = Race.objects.get_or_create(
                name=race_name,
                defaults={"description": race_description}
            )

            for skill in data["race"]["skills"]:
                print(skill["name"])
                print(skill["bonus"])
                skill_name = skill["name"]
                skill_bonus = skill["bonus"]

                skill_obj, created = Skill.objects.get_or_create(
                    name=skill_name,
                    defaults={
                        "bonus": skill_bonus,
                        "race": race,
                    }
                )
            guild = None

            if data["guild"] is not None:
                guild_name = data["guild"]["name"]
                guild_description = data["guild"]["description"]

                guild, created = Guild.objects.get_or_create(
                    name=guild_name,
                    defaults={"description": guild_description}
                )

            player_email = data["email"]
            player_bio = data["bio"]
            player_obj, created = Player.objects.get_or_create(
                nickname=player,
                defaults={
                    "email": player_email,
                    "bio": player_bio,
                    "guild": guild,
                    "race": race,
                }
            )
            for skill in data["race"]["skills"]:
                skill_obj = Skill.objects.get(name=skill["name"])
                player_obj.skills.add(skill_obj)


if __name__ == "__main__":
    main()
