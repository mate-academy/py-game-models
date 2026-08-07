import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild
import json


def main() -> None:

    with open("players.json", "r") as file:
        players_data = json.load(file)

    for player, data in players_data.items():

        race_data = data["race"]
        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data["description"]}
        )

        for skill_data in race_data.get("skills", []):
            Skill.objects.get_or_create(
                name=skill_data["name"],
                race=race,
                defaults={"bonus": skill_data["bonus"]}
            )

        guild_data = data.get("guild")
        guild = None
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data.get("description")}
            )

        player, _ = Player.objects.get_or_create(
            nickname=player,
            defaults={
                "email": data["email"],
                "bio": data["bio"],
                "race": race,
                "guild": guild
            }
        )


if __name__ == "__main__":
    main()
