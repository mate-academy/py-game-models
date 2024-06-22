import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    Guild.objects.all().delete()
    Skill.objects.all().delete()
    Race.objects.all().delete()
    Player.objects.all().delete()

    with open("players.json") as file:
        players = json.load(file)

        for name, player_info in players.items():
            race_info = player_info["race"]
            race, _ = Race.objects.get_or_create(
                name=race_info["name"],
                description=race_info["description"]
            )

            skill_info = race_info["skills"]
            for skill in skill_info:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )

            guild_info = player_info["guild"]
            guild = None
            if guild_info:
                guild, _ = Guild.objects.get_or_create(
                    name=guild_info["name"],
                    description=guild_info["description"]
                )

            Player.objects.get_or_create(
                nickname=name,
                email=player_info["email"],
                bio=player_info["bio"],
                race=race,
                guild=guild
            )


if __name__ == "__main__":
    main()
