import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as f:
        players = json.load(f)

    for player_name, player_data in players.items():
        race_data = player_data.get("race")
        race, _ = Race.objects.get_or_create(name=race_data["name"],
                                             defaults={"description": race_data["description"]})

        for skill_data in race_data.get("skills"):
            Skill.objects.get_or_create(name=skill_data["name"],
                                        defaults={"bonus": skill_data["bonus"], "race": race})

        guild_data = player_data.get("guild")
        if guild_data is not None:
            guild, _ = Guild.objects.get_or_create(name=guild_data["name"],
                                                   defaults={"description": guild_data["description"]})
        else:
            guild = None

        Player.objects.create(
            nickname=player_name,
            email=player_data.get("email"),
            bio=player_data.get("bio"),
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
