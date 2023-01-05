import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_file:
        players_data = json.load(players_file)

    for player in players_data:
        player_nickname = player
        player_email = players_data[player]["email"]
        player_bio = players_data[player]["bio"]
        race = players_data[player]["race"]

        if Race.objects.filter(name=race["name"]).exists():
            player_race = Race.objects.get(name=race["name"])
        else:
            player_race = Race.objects.create(
                name=race["name"],
                description=race["description"]
            )

        skills = race["skills"]

        for skill in skills:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=player_race
                )

        guild = players_data[player]["guild"]

        if guild is not None:
            if not Guild.objects.filter(name=guild["name"]).exists():
                Guild.objects.create(
                    name=guild["name"],
                    description=guild["description"]
                )
            player_guild = Guild.objects.get(name=guild["name"])
        else:
            player_guild = guild

        Player.objects.create(
            nickname=player_nickname,
            email=player_email,
            bio=player_bio,
            race=player_race,
            guild=player_guild
        )


if __name__ == "__main__":
    main()
