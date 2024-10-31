import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    players = {}
    with open("players.json") as file:
        players = json.load(file)

    for player, info in players.items():
        email, bio, race, guild = info.values()
        skills = race["skills"]

        race, _ = Race.objects.get_or_create(
            name=race["name"],
            description=race["description"],
        )

        if skills and not race.skill_set.all():
            for skill in skills:
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )

        if guild:
            guild_description = (
                guild["description"] if guild["description"] else None
            )
            guild, _ = Guild.objects.get_or_create(
                name=guild["name"],
                description=guild_description,
            )

        Player.objects.create(
            nickname=player,
            email=email,
            bio=bio,
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
