import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for nickname, player in players.items():
        guild = player["guild"]
        race = player["race"]
        guild_db = None
        race_db = None

        if guild:
            guild_db, _ = Guild.objects.get_or_create(
                name=guild["name"], description=guild.get("description", ""))

        if race:
            race_db, _ = Race.objects.get_or_create(
                name=race["name"], description=race.get("description", ""))

            if race.get("skills"):
                for skill in race["skills"]:
                    Skill.objects.get_or_create(
                        name=skill["name"], bonus=skill["bonus"],
                        race=race_db)

        Player.objects.get_or_create(
            nickname=nickname,
            email=player["email"], bio=player["bio"],
            race=race_db, guild=guild_db)


if __name__ == "__main__":
    main()
