import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    # Player.objects.all().delete()
    # Skill.objects.all().delete()
    # Guild.objects.all().delete()
    # Race.objects.all().delete()

    with open("players.json") as players_data:
        players = json.load(players_data)

    for player in players:
        player_race = Race.objects.get_or_create(
            name=players[player]["race"]["name"],
            description=players[player]["race"]["description"]
        )[0]
        player_guild = Guild.objects.get_or_create(
            name=players[player]["guild"]["name"],
            description=players[player]["guild"]["description"])[0] \
            if players[player]["guild"] else None

        Player.objects.create(
            nickname=player,
            email=players[player]["email"],
            bio=players[player]["bio"],
            race=player_race,
            guild=player_guild
        )

        for skill in players[player]["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=player_race
            )[0]


if __name__ == "__main__":
    main()
