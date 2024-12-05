import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for player_name, player_data in data.items():
        race_data = player_data.get("race")
        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            description=race_data.get("description", "")
        )

        for skill_data in race_data.get("skills", []):
            skill, _ = Skill.objects.get_or_create(
                name=skill_data["name"],
                bonus=skill_data["bonus"],
                race=race
            )

        guild_data = player_data.get("guild")
        if guild_data:
            guild_name = guild_data.get("name")
            guild_description = guild_data.get("description")

            guild, _ = Guild.objects.get_or_create(
                name=guild_name,
                defaults={"description": guild_description}
            )

        player, _ = Player.objects.get_or_create(
            nickname=player_name,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race,
            guild=guild if guild_data else None
        )


if __name__ == "__main__":
    main()
