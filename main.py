import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild

import json


def main() -> None:
    try:
        with open("players.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("File 'players.json' not found.")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return

    for person, res in data.items():
        race_data, created = Race.objects.get_or_create(
            name=res["race"]["name"],
            defaults={"description": res["race"].get("description", "")}
        )

        guild_data = res.get("guild")
        if guild_data is not None:
            guild_data, created = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data.get("description", "")}
            )

        skill_info = res["race"].get("skills", [])
        if skill_info:
            for skill_data in skill_info:
                Skill.objects.get_or_create(
                    name=skill_data["name"],
                    defaults={
                        "bonus": skill_data.get("bonus", ""),
                        "race": race_data}
                )

        player, player_created = Player.objects.get_or_create(
            nickname=person,
            email=res["email"],
            defaults={"bio": res["bio"], "race": race_data, "guild": guild_data}
        )

        if not player_created:
            player.bio = res["bio"]
            player.race = race_data
            player.guild = guild_data
            player.save()


if __name__ == "__main__":
    main()
