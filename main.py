import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for nickname, data in players.items():
        email = data.get("email")
        bio = data.get("bio")
        race = data.get("race")
        skills = race.get("skills")
        guild = data.get("guild")

        new_race, race_created = Race.objects.get_or_create(
            name=race.get("name"),
            description=race.get("description")
        )

        if race_created:
            for skill in skills:
                Skill.objects.get_or_create(
                    name=skill.get("name"),
                    bonus=skill.get("bonus"),
                    race=new_race
                )

        new_guild = None
        if guild:
            new_guild, guild_created = Guild.objects.get_or_create(
                name=guild.get("name"),
                description=guild.get("description")
            )

        player = Player(
            nickname=nickname,
            email=email,
            bio=bio,
            race=new_race,
            guild=new_guild
        )

        player.save()


if __name__ == "__main__":
    main()
