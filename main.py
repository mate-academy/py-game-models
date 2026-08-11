import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        players = json.load(f)

    for player in players:
        player_race, created = Race.objects.get_or_create(
            name=players.get(player)["race"]["name"],
            description=players.get(player)["race"]["description"],
        )

        for skill in players.get(player)["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=player_race,
            )
        if players.get(player)["guild"]:
            player_guild, created = Guild.objects.get_or_create(
                name=players.get(player)["guild"]["name"],
                description=players.get(player)["guild"]["description"]
            )
        else:
            player_guild = None

        Player.objects.get_or_create(
            nickname=player,
            email=players.get(player)["email"],
            bio=players.get(player)["bio"],
            race=player_race,
            guild=player_guild
        )


if __name__ == "__main__":
    main()
