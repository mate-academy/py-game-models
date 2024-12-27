import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open('players.json', 'r') as f:
        data = json.load(f)

    for player_name, player_data in data.items():
        race_name = player_data["race"]["name"]
        race_description = player_data["race"]["description"]
        race, _ = Race.objects.get_or_create(name=race_name, description=race_description)

        for skill_data in player_data["race"]["skills"]:
            skill_name = skill_data["name"]
            skill_bonus = skill_data["bonus"]
            Skill.objects.get_or_create(name=skill_name, bonus=skill_bonus, race=race)

        guild = None
        if player_data["guild"]:
            guild_name = player_data["guild"]["name"]
            guild_description = player_data["guild"]["description"]
            guild, _ = Guild.objects.get_or_create(name=guild_name, description=guild_description)

        Player.objects.get_or_create(
            nickname=player_name,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race,
            guild=guild
        )

if __name__ == "__main__":
    Player.objects.all().delete()
    Race.objects.all().delete()
    Skill.objects.all().delete()
    Guild.objects.all().delete()
    main()
