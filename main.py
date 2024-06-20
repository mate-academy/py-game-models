import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        data = json.load(file)

    for player_name, player_data in data.items():
        race_data = player_data["race"]
        race, created = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data.get("description", "")}
        )

        for skill_info in race_data.get_("skills", []):
            skill, created = Skill.objects.get_or_create(
                name=skill_info["name"],
                defaults={"bonus": skill_info["bonus"], "race": race}
            )

        guild_info = player_data.get("guild")
        guild = None
        if guild_info:
            guild, created = Guild.objects.get_or_create(
                name=guild_info["name"],
                defaults={"description": guild_info.get("description", "")}
            )

        Player.objects.create(
            nickname=player_name,
            email=player_data["email"],
            bio=player_data.get("bio", ""),
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
