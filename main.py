import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        users_data = json.load(file)
    for player_nickname, player_data in users_data.items():
        (player_email,
         player_bio,
         race,
         guild) = player_data.values()
        race_name = race.get("name")
        race_description = race.get("description")
        skills = race.get("skills")

        race_instance, _ = Race.objects.get_or_create(
            name=race_name,
            description=race_description
        )
        if skills:
            for skill in skills:
                Skill.objects.get_or_create(
                    name=skill.get("name"),
                    bonus=skill.get("bonus"),
                    race=race_instance
                )
        if guild:
            guild_name = guild.get("name")
            guild_description = guild.get("description")
            guild_instance, _ = Guild.objects.get_or_create(
                name=guild_name,
                description=guild_description
            )
        else:
            guild_instance = None
        Player.objects.get_or_create(
            nickname=player_nickname,
            email=player_email,
            bio=player_bio,
            race=race_instance,
            guild=guild_instance
        )


if __name__ == "__main__":
    main()
