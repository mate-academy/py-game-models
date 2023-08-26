import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as json_file:
        data = json.load(json_file)

    for player_name, entry in data.items():
        race_data = entry["race"]
        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            description=race_data["description"]
        )

        guild_data = entry["guild"]
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                description=guild_data["description"]
            )
        else:
            guild = None

        player_data = {
            "nickname": player_name,
            "email": entry["email"],
            "bio": entry["bio"],
            "race": race,
            "guild": guild,
        }

        player, _ = Player.objects.get_or_create(
            nickname=player_name,
            defaults=player_data
        )

        for skill_entry in race_data["skills"]:
            skill, _ = Skill.objects.get_or_create(
                name=skill_entry["name"],
                bonus=skill_entry["bonus"],
                race=race
            )


if __name__ == "__main__":
    main()
