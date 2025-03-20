import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players_data = json.load(file)

    for nickname, player_data in players_data.items():
        race_info = player_data["race"]
        race, _ = Race.objects.get_or_create(
            name=race_info["name"],
            defaults={"description": race_info.get("description", "")},
        )

        skills = [
            Skill.objects.get_or_create(
                name=skill["name"],
                race=race,  # ✅ Додаємо race, щоб уникнути NULL
                defaults={"bonus": skill.get("bonus", "")},
            )[0]
            for skill in race_info.get("skills", [])
        ]

        guild_data = player_data.get("guild")
        guild = None
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data.get("description", "")},
            )

        player_obj, created = Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": player_data["email"],
                "bio": player_data.get("bio", ""),
                "guild": guild,
                "race": race,
            },
        )

        if created:
            player_obj.skills.add(*skills)


if __name__ == "__main__":
    main()
