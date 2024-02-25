import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for nickname, player_data in players.items():
        player_race = Race.objects.get_or_create(
            name=player_data["race"]["name"],
            description=player_data["race"]["description"],
        )[0]

        player_guild = Guild.objects.get_or_create(
            name=player_data["guild"]["name"],
            description=player_data["guild"]["description"],
        )[0] if player_data.get("guild") else None

        for skill in player_data["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=player_race,
            )

        Player.objects.get_or_create(
            nickname=nickname,
            email=player_data["email"],
            bio=player_data["bio"],
            race=player_race,
            guild=player_guild,
        )


if __name__ == "__main__":
    main()
