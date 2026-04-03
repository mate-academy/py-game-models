import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", encoding="utf-8") as f:
        players_data = json.load(f)

    for nickname, data in players_data.items():
        race_data = data["race"]
        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data.get("description", "")}
        )
        skills = race_data.get("skills")
        if skills:
            for s_data in race_data["skills"]:
                Skill.objects.get_or_create(
                    name=s_data["name"],
                    race=race,
                    defaults={"bonus": s_data["bonus"]}
                )

        guild = None
        if data.get("guild"):
            guild_data = data["guild"]
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data.get("description")}
            )

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": data["email"],
                "bio": data["bio"],
                "race": race,
                "guild": guild
            }
        )


if __name__ == "__main__":
    main()
