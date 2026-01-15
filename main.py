import json
from init_django_orm import setup_django
from db.models import Race, Skill, Guild, Player

setup_django()


def main() -> None:
    with open("players.json", encoding="utf-8") as file:
        players_data = json.load(file)

    for nickname, player in players_data.items():
        race_data = player.get("race", {})
        race_obj, _ = Race.objects.get_or_create(
            name=race_data.get("name"),
            defaults={"description": race_data.get("description", "")}
        )

        for skill in race_data.get("skills", []):
            Skill.objects.get_or_create(
                name=skill.get("name"),
                race=race_obj,
                defaults={"bonus": skill.get("bonus", "")}
            )

        guild_data = player.get("guild")
        guild_obj = None
        if guild_data:
            guild_obj, _ = Guild.objects.get_or_create(
                name=guild_data.get("name"),
                defaults={"description": guild_data.get("description", "")}
            )

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": player.get("email"),
                "bio": player.get("bio", ""),
                "race": race_obj,
                "guild": guild_obj,
            }
        )


if __name__ == "__main__":
    main()
