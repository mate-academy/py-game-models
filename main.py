import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r", encoding="utf-8") as file:
        players_data = json.load(file)

    for player_name, player_info in players_data.items():
        race_data = player_info["race"]
        try:
            race_obj = Race.objects.get(name=race_data["name"])
        except Race.DoesNotExist:
            race_obj = Race.objects.create(
                name=race_data["name"],
                description=race_data["description"]
            )
        guild_obj = None
        if player_info["guild"]:
            guild_data = player_info["guild"]
            try:
                guild_obj = Guild.objects.get(name=guild_data["name"])
            except Guild.DoesNotExist:
                guild_obj = Guild.objects.create(
                    name=guild_data["name"],
                    description=guild_data["description"]
                )
        skill_objects = []
        for skill in race_data["skills"]:
            try:
                skill_obj = Skill.objects.get(
                    name=skill["name"],
                    race=race_obj
                )
            except Skill.DoesNotExist:
                skill_obj = Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race_obj
                )
            skill_objects.append(skill_obj)
        try:
            player_obj = Player.objects.get(nickname=player_name)
        except Player.DoesNotExist:
            player_obj = Player.objects.filter(nickname=player_name).first()
            if not player_obj:
                player_obj = Player.objects.create(
                    nickname=player_name,
                    email=player_info["email"],
                    bio=player_info["bio"],
                    race=race_obj,
                    guild=guild_obj
                )
            player_obj.skills.set(skill_objects)
    return Player.objects.all()


if __name__ == "__main__":
    main()
