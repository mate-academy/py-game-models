import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        info = json.load(file)

    for key, value in info.items():
        race_data = value["race"]
        race, created = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data["description"]}
        )

        for skill_data in race_data.get("skills", []):
            skill, created = Skill.objects.get_or_create(
                name=skill_data["name"],
                defaults={"bonus": skill_data["bonus"], "race": race}
            )

    for key, value in info.items():
        guild_data = value.get("guild")
        if guild_data:
            guild, created = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data.get("description", "")}
            )

    for key, value in info.items():
        race = Race.objects.get(name=value["race"]["name"])
        guild = None
        if value.get("guild"):
            guild = Guild.objects.get(name=value["guild"]["name"])

        Player.objects.get_or_create(
            nickname=key,
            defaults={
                "email": value["email"],
                "bio": value["bio"],
                "race": race,
                "guild": guild,
#                "created_at": datetime.now()
            }
        )


if __name__ == "__main__":
    main()
