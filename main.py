import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild

import json


def main() -> None:
    with open("players.json") as file:
        data = json.load(file)

    for player_name, player_info in data.items():
        race_info = player_info.get("race")
        if race_info:
            race, created = Race.objects.get_or_create(
                name=race_info.get("name"),
                description=race_info.get("description")
            )

        guild = player_info.get("guild")
        if guild:
            guild, created = Guild.objects.get_or_create(
                name=guild.get("name"),
                description=guild.get("description")
            )

        skill_info = race_info.get("skills")
        if skill_info:
            for skill in skill_info:
                Skill.objects.get_or_create(
                    name=skill.get("name"),
                    bonus=skill.get("bonus"),
                    race=race
                )

        player, player_created = Player.objects.get_or_create(
            nickname=player_name,
            email=player_info.get("email"),
            defaults={
                "bio": player_info.get("bio"), "race": race, "guild": guild
            }
        )

        if not player_created:
            player.bio = player_info.get("bio")
            player.race = race
            player.guild = guild
            player.save()


if __name__ == "__main__":
    main()
