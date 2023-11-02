import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as json_file:
        players = json.load(json_file)

    for key_nickname, value in players.items():
        race_data = value.get("race")
        if race_data:
            race, created = Race.objects.get_or_create(
                name=race_data.get("name"),
                description=race_data.get("description")
            )

            if created:
                race.save()

        guild_data = value.get("guild")
        if guild_data:
            guild, created = Guild.objects.get_or_create(
                name=guild_data.get("name"),
                description=guild_data.get("description")
            )

            if created:
                guild.save()

        skills = value.get("race").get("skills")
        if skills:
            for skill_data in skills:
                skill, created = Skill.objects.get_or_create(
                    name=skill_data.get("name"),
                    bonus=skill_data.get("bonus"),
                    race=race
                )

                if created:
                    skill.save()

        player = Player.objects.create(
            nickname=key_nickname,
            email=value.get("email"),
            bio=value.get("bio"),
            race=race,
            guild=guild if guild_data else None
        )
        player.save()


if __name__ == "__main__":
    main()
