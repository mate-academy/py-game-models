import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as player_file:
        players = json.load(player_file)

    for nickname, player in players.items():
        race, _ = Race.objects.get_or_create(
            name=player["race"]["name"],
            description=player["race"]["description"]
        )

        for skill in player["race"]["skills"]:
            Skill.objects.get_or_create(
                **skill,
                race=race
            )

        if player.get("guild"):
            guild, _ = Guild.objects.get_or_create(**player["guild"])

        else:
            guild = None

        player, created = Player.objects.get_or_create(
            nickname=nickname,
            email=player["email"],
            bio=player["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
