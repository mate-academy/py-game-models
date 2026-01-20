import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        data = json.load(file)

    for player, details in data.items():
        race_data = details["race"]
        race, created_race = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data["description"]}
        )

        for skill_data in race_data["skills"]:
            skill, created_skill = Skill.objects.get_or_create(
                name=skill_data["name"],
                defaults={"bonus": skill_data["bonus"]}
            )
            race.skill_set.add(skill)

        guild_data = details["guild"]
        if guild_data:
            Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data.get("description")}
            )

        Player.objects.get_or_create(
            nickname=player,
            defaults={
                "email": details["email"],
                "bio": details["bio"],
                "race": race,
                "guild": Guild.objects.filter(
                    name=guild_data["name"]).first() if guild_data else None
            }
        )


if __name__ == "__main__":
    main()
