import json
import init_django_orm  # noqa: F401


from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        data = json.load(f)

    for nickname, info in data.items():
        race_data = info["race"]
        race_obj, created = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data.get("description", "")}
        )

        for skill_data in race_data.get("skills", []):
            Skill.objects.get_or_create(
                name=skill_data["name"],
                race=race_obj,
                defaults={"bonus": skill_data["bonus"]}
            )

        guild_obj = None
        if info.get("guild"):
            guild_data = info["guild"]
            guild_obj, created = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data.get("description")}
            )

        Player.objects.get_or_create(
            nickname=nickname,
            email=info["email"],
            defaults={
                "bio": info.get("bio", ""),
                "race": race_obj,
                "guild": guild_obj
            }
        )


if __name__ == "__main__":
    main()
