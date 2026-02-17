import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        players = json.load(f)

    for key, value in players.items():
        race, race_created = Race.objects.get_or_create(
            name=value["race"]["name"],
            defaults={
                "description": value["race"]["description"],
            })
        if race_created:
            race.save()

        for skill in value["race"]["skills"]:
            skill, skill_created = Skill.objects.get_or_create(
                name=skill["name"],
                defaults={
                    "bonus": skill["bonus"],
                    "race": race,
                })
            if skill_created:
                skill.save()

        value_guild = value.get("guild", None)
        if value_guild is not None:
            guild, guild_created = Guild.objects.get_or_create(
                name=value_guild["name"],
                defaults={
                    "description": value_guild["description"],
                })
            if guild_created:
                guild.save()
        else:
            guild = None

        player, player_created = Player.objects.get_or_create(
            nickname=key,
            defaults={
                "email": value["email"],
                "bio": value["bio"],
                "race": race,
                "guild": guild,
            })
        if player_created:
            player.save()


if __name__ == "__main__":
    main()
