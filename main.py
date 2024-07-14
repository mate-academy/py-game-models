import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    # Load data from players.json
    with open("players.json") as file:
        players_data = json.load(file)

    for player, data in players_data.items():
        email = data["email"]
        bio = data["bio"]
        race_data = data["race"]
        guild_data = data.get("guild")
        skills_data = race_data.get("skills", [])

        # Get or create Race
        race, created = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data.get("description", "")}
        )

        # Get or create Guild
        if guild_data:
            guild, created = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data.get("description", "")}
            )
        else:
            guild = None

        # Get or create Skills and associate with the Race
        for skill_data in skills_data:
            skill, created = Skill.objects.get_or_create(
                name=skill_data["name"],
                defaults={"bonus": skill_data["bonus"], "race": race}
            )

            if not created:
                skill.race = race
                skill.save()

        # Create Player
        Player.objects.create(
            nickname=player,
            email=email,
            bio=bio,
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
