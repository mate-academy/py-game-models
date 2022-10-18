import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for player, data in players.items():

        player_email = data["email"]
        player_bio = data["bio"]
        player_race = data["race"]
        player_guild = data["guild"]
        player_skills = player_race["skills"]

        if not Race.objects.filter(name=player_race["name"]).exists():
            Race.objects.create(
                name=player_race["name"],
                description=player_race["description"]
            )
        player_race = Race.objects.get(name=player_race["name"])

        if player_guild:
            if not Guild.objects.filter(name=player_guild["name"]).exists():
                Guild.objects.create(
                    name=player_guild["name"],
                    description=player_guild["description"]
                )
            player_guild = Guild.objects.get(name=player_guild["name"])

        if player_skills:
            for skill in player_skills:
                if not Skill.objects.filter(name=skill["name"]).exists():
                    Skill.objects.create(
                        name=skill["name"],
                        bonus=skill["bonus"],
                        race=player_race,
                    )
        if not Player.objects.filter(nickname=player).exists():
            Player.objects.create(
                nickname=player,
                email=player_email,
                bio=player_bio,
                race=player_race,
                guild=player_guild,
            )


if __name__ == "__main__":
    main()
