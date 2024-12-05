import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for nickname, player in data.items():

        race_db, _ = Race.objects.get_or_create(
            name=player["race"]["name"],
            description=player["race"]["description"]
        )

        guild_db = None
        if player["guild"]:
            guild_db, _ = Guild.objects.get_or_create(
                name=player["guild"]["name"],
                description=player["guild"]["description"]
            )

        for skill in player["race"]["skills"]:
            skill_db, _ = Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race_db
            )

        player_db, _ = Player.objects.get_or_create(
            nickname=nickname,
            email=player["email"],
            bio=player["bio"],
            race=race_db,
            guild=guild_db,
        )


if __name__ == "__main__":
    main()
