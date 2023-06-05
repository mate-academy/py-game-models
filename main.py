import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        player_data = json.load(f)

    for name in player_data:
        player = player_data[name]
        email, bio = player["email"], player["bio"]
        race_data, guild = player["race"], player["guild"]
        skills_data = race_data["skills"]

        race, is_created_race = Race.objects.get_or_create(
            name=f"{race_data['name']}",
            description=f"{race_data['description']}"
        )

        if skills_data:
            for skill in skills_data:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )

        if guild:
            guild, is_created_guild = Guild.objects.get_or_create(
                name=guild["name"],
                description=guild["description"]
            )

        Player.objects.create(
            nickname=name,
            email=email,
            bio=bio,
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
    # Player.objects.all().delete()
    # Race.objects.all().delete()
    # Skill.objects.all().delete()
    # Guild.objects.all().delete()
