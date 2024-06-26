import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players = json.load(file)

        for nickname, person in players.items():
            race_info = person["race"]

            race, _ = Race.objects.get_or_create(
                name=race_info["name"],
                description=race_info["description"]
            )

            for skill in race_info["skills"]:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )
                
            guild = None
            guild_info = person["guild"]
            if guild_info:
                guild, created = Guild.objects.get_or_create(
                    name=guild_info["name"],
                    description=guild_info["description"]
                )

            Player.objects.get_or_create(
                nickname=nickname,
                email=person["email"],
                bio=person["bio"],
                race=race,
                guild=guild,
            )

if __name__ == "__main__":
    main()
