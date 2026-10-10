import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for player_key, player_values in players.items():
        guild_value = player_values.get("guild")
        race_value = player_values.get("race")

        if guild_value is not None:
            guild, _ = Guild.objects.get_or_create(
                name=guild_value.get("name"),
                description=guild_value.get("description")
            )
        else:
            guild = None

        race, _ = Race.objects.get_or_create(
            name=race_value.get("name"),
            description=race_value.get("description")
        )

        for skill in race_value.get("skills"):
            Skill.objects.get_or_create(
                name=skill.get("name"),
                bonus=skill.get("bonus"),
                race=race
            )

        Player.objects.create(
            nickname=player_key,
            email=player_values.get("email"),
            bio=player_values.get("bio"),
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
