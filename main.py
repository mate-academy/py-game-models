import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players_data = json.load(file)
    for nickname, player_info in players_data.items():
        race, _ = Race.objects.get_or_create(
            name=player_info["race"]["name"],
            defaults={"description": player_info["race"]["description"]}
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
        guild = None
        if player_info["guild"] is not None:
            guild, _ = Guild.objects.get_or_create(
                name=player_info["guild"]["name"],
                description=player_info["guild"]["description"]
            )
        Player.objects.get_or_create(
            nickname=nickname,
            email=player_info["email"],
            bio=player_info["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
