import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)
    for player in data:
        player_data = data[player]
        race_data = player_data.get("race")
        if not race_data:
            continue
        race, _ = Race.objects.get_or_create(
            name=race_data.get("name", ""),
            defaults={"description": race_data.get("description", "")},
        )
        guild_data = player_data.get("guild")
        if guild_data:
            guild = Guild.objects.get_or_create(
                name=guild_data.get("name", ""),
                defaults={"description": guild_data.get("description")},
            )[0]
        else:
            guild = None

        for skill in race_data.get("skills", []):
            Skill.objects.get_or_create(
                name=skill.get("name", ""),
                defaults={"bonus": skill.get("bonus", ""), "race": race},
            )

        Player.objects.get_or_create(
            nickname=player,
            defaults={
                "email": player_data.get("email", ""),
                "bio": player_data.get("bio"),
                "race": race,
                "guild": guild,
            },
        )


if __name__ == "__main__":
    main()
