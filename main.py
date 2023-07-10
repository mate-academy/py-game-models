import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:

    with open("players.json", "r") as players:
        data = json.load(players)

    for key, value in data.items():
        players_race = Race.objects.get(
            name=value["race"]["name"]
        ) if Race.objects.filter(
            name=value["race"]["name"]
        ).exists() else Race(
            name=value["race"]["name"],
            description=value["race"]["description"]
        )
        players_race.save()

        if value["guild"]:
            players_guild = Guild.objects.get(
                name=value["guild"]["name"]
            ) if Guild.objects.filter(
                name=value["guild"]["name"]
            ).exists() else Guild(
                name=value["guild"]["name"],
                description=value["guild"]["description"]
            )
            players_guild.save()
        else:
            players_guild = None

        for skill in value["race"]["skills"]:
            if skill and not Skill.objects.filter(name=skill["name"]).exists():
                new_skill = Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=players_race
                )
                new_skill.save()

        new_player = Player(
            nickname=key,
            email=value["email"],
            bio=value["bio"],
            race=players_race,
            guild=players_guild
        )
        new_player.save()


if __name__ == "__main__":
    main()
