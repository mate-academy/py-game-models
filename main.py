from json import load

import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = load(file)
    for player, data in data.items():
        race = data.get("race")
        skills = data.get("race").get("skills")
        guild = data.get("guild")

        race, _ = Race.objects.get_or_create(
            name=race.get("name"),
            description=race.get("description")
        )

        for skill in skills:
            Skill.objects.get_or_create(
                name=skill.get("name"),
                bonus=skill.get("bonus"),
                race=race
            )

        if guild:
            guild, _ = Guild.objects.get_or_create(
                name=guild.get("name"),
                description=guild.get("description")
            )

        player = Player(
            nickname=player,
            email=data.get("email"),
            bio=data.get("bio"),
            race=race,
            guild=guild
        )
        player.save()


if __name__ == "__main__":
    main()
