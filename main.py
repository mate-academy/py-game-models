import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    players = {}
    with open("./players.json", "r") as file:
        players = json.load(file)

    for player_key, player_value in players.items():
        new_player = Player(
            nickname=player_key,
            email=player_value["email"],
            bio=player_value["bio"])

        race = player_value.get("race")
        if race:
            new_race, _ = Race.objects.get_or_create(
                name=race["name"],
                description=race["description"]
            )

            skills = race.get("skills")
            if skills:
                for skill in skills:
                    new_skill, _ = Skill.objects.get_or_create(
                        name=skill["name"],
                        bonus=skill["bonus"],
                        race=new_race
                    )

            new_player.race = new_race

        guild = player_value.get("guild")
        if guild:
            new_guild, _ = Guild.objects.get_or_create(
                name=guild["name"],
                description=guild["description"]
            )

            new_player.guild = new_guild

        new_player.save()


if __name__ == "__main__":
    main()
