import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players: dict = json.load(file)

    for name, player in players.items():
        race, _ = Race.objects.get_or_create(
            name=player.get("race", {}).get("name"),
            defaults={
                "description": player.get("race", {}).get("description")
            },
        )

        for skill in player.get("race", {}).get("skills", []):
            Skill.objects.get_or_create(
                name=skill.get("name"),
                defaults={"bonus": skill.get("bonus"), "race": race}
            )

        guild_data = player.get("guild")
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data.get("name"),
                defaults={"description": guild_data.get("description")},
            )
        else:
            guild = None

        Player.objects.get_or_create(
            nickname=name,
            defaults={
                "email": player.get("email"),
                "bio": player.get("bio"),
                "race": race,
                "guild": guild,
            },
        )


if __name__ == "__main__":
    main()
