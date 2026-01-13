import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r", encoding="utf-8") as file:
        data = json.load(file)

        for nickname, player_info in data.items():
            race_info = player_info["race"]
            race, _ = Race.objects.get_or_create(
                name=race_info["name"],
                defaults={"description": race_info.get("description", "")},
            )
            for skill_info in race_info["skills"]:
                skill, _ = Skill.objects.get_or_create(
                    name=skill_info["name"],
                    defaults={"bonus": skill_info.get("bonus", "")},
                    race=race
                )

            guild_info = player_info.get("guild")
            if guild_info:
                guild, _ = Guild.objects.get_or_create(
                    name=guild_info["name"],
                    defaults={"description": guild_info.get("description")},
                )
            else:
                guild = None

            Player.objects.get_or_create(
                nickname=nickname,
                defaults={
                    "email": player_info["email"],
                    "bio": player_info["bio"],
                    "race": race,
                    "guild": guild, }
            )


if __name__ == "__main__":
    main()
