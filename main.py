import json
from django.utils import timezone
from db.models import Guild, Race, Skill, Player


def main() -> None:
    with open("players.json") as file:
        player_data = json.load(file)

        for player_name, player_info in player_data.items():
            race, created = Race.objects.get_or_create(
                name=player_info["race"]["name"],
                defaults={"description": player_info["race"]["description"]}
            )

            guild_info = player_info["guild"]
            if guild_info:
                guild, created = Guild.objects.get_or_create(
                    name=guild_info["name"],
                    defaults={"description": guild_info.get("description", "")}
                )
            else:
                guild = None

            Player.objects.get_or_create(
                nickname=player_name,
                email=player_info["email"],
                bio=player_info["bio"],
                race=race,
                guild=guild,
                created_at=timezone.now()
            )

            for skill_dt in player_info["race"]["skills"]:
                Skill.objects.get_or_create(
                    name=skill_dt["name"],
                    bonus=skill_dt["bonus"],
                    race=race
                )


if __name__ == "__main__":
    main()
