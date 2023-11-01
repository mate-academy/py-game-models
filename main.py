import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def get_players(filename: str) -> dict:
    with open(filename) as file:
        return json.load(file)


def main() -> None:
    players = get_players("players.json")

    for nickname, player_info in players.items():
        race, _ = Race.objects.get_or_create(
            name=player_info["race"]["name"],
            description=player_info["race"]["description"]
        )
        for skill in player_info["race"]["skills"]:
            Skill.objects.get_or_create(
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
