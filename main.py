import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players:
        players = json.load(players)

    for player_name, player in players.items():
        race, _ = Race.objects.get_or_create(
            name=player["race"]["name"],
            description=player["race"]["description"]
        )

        for skill_list in player["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill_list["name"],
                bonus=skill_list["bonus"],
                race=race
            )

        guild, _ = Guild.objects.get_or_create(
            name=player["guild"]["name"],
            description=player["guild"]["description"]
        ) if player["guild"] else (None, False)

        Player.objects.get_or_create(
            nickname=player_name,
            email=player["email"],
            bio=player["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
