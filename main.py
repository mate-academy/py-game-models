import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as players_f:
        players = json.load(players_f)

    for nickename, option in players.items():
        player_to_create = Player(
            nickname=nickename,
            email=option.get("email"),
            bio=option.get("bio"),
        )

        race, _ = Race.objects.get_or_create(
            name=option.get("race").get("name"),
            description=option.get("race").get("description")
        )
        player_to_create.race = race

        if skills := option.get("race").get("skills"):
            for skill in skills:
                Skill.objects.get_or_create(
                    name=skill.get("name"),
                    bonus=skill.get("bonus"),
                    race=race
                )

        if guild := option.get("guild"):
            guild, _ = Guild.objects.get_or_create(
                name=guild.get("name"),
                description=guild.get("description")
            )
            player_to_create.guild = guild

        player_to_create.save()


if __name__ == "__main__":
    main()
