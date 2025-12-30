import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for player_name, player_data in players.items():
        race, _ = Race.objects.get_or_create(
            name=player_data["race"]["name"],
            defaults={"description": player_data["race"]["description"]},
        )

        for skill_data in player_data["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill_data["name"],
                bonus=skill_data["bonus"],
                race=race,
            )

        guild = None
        if guild_data := player_data.get("guild"):
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data["description"]},
            )

        Player.objects.get_or_create(
            nickname=player_name,
            defaults={
                "email": player_data["email"],
                "bio": player_data["bio"],
                "race": race,
                "guild": guild,
            }

        )


if __name__ == "__main__":
    main()
