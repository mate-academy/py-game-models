import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_file:
        players_data = json.load(players_file)

        for player_name, info in players_data.items():

            race_obj, race = Race.objects.get_or_create(
                name=info["race"]["name"],
                description=info["race"]["description"]
            )

            skills_data = (info["race"]["skills"] if
                           info["race"]["skills"] else None)

            if skills_data is not None:
                for skill in skills_data:
                    Skill.objects.get_or_create(
                        name=skill["name"],
                        bonus=skill["bonus"],
                        race_id=race_obj.id
                    )

            guild_data = info["guild"] if info["guild"] else None
            if guild_data is not None:
                guild_obj, guild = Guild.objects.get_or_create(
                    name=info["guild"]["name"],
                    description=info["guild"]["description"]
                )
            else:
                guild_obj = None

            guild_id = guild_obj.id if guild_obj else None

            Player.objects.get_or_create(
                nickname=player_name,
                email=info["email"],
                bio=info["bio"],
                race_id=race_obj.id,
                guild_id=guild_id
            )


if __name__ == "__main__":
    main()
