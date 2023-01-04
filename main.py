import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    players_data = None

    with open("players.json", "r") as source_file:
        players_data = json.load(source_file)

    for nickname, player_info in players_data.items():
        race = Race.objects.filter(
            name=player_info["race"]["name"]
        ).first()

        if not race:
            race = Race.objects.create(
                name=player_info["race"]["name"],
                description=player_info["race"]["description"]
            )

        for skill in player_info["race"]["skills"]:
            if not Skill.objects.filter(
                name=skill["name"]
            ).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )

        guild = Guild.objects.filter(
            name=player_info["guild"]["name"]
        ).first() if player_info["guild"] else None

        if player_info["guild"] and not guild:
            guild = Guild.objects.create(
                name=player_info["guild"]["name"],
                description=player_info["guild"]["description"]
            )

        Player.objects.create(
            nickname=nickname,
            email=player_info["email"],
            bio=player_info["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
