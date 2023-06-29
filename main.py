import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as config_players:
        players = json.load(config_players)

    for player_name, player_info in players.items():
        config_race = player_info["race"]
        config_guild = player_info["guild"]

        race, is_race_created = Race.objects.get_or_create(
            name=config_race["name"],
            description=config_race["description"]
        )

        if is_race_created:
            for skill in player_info["race"]["skills"]:
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )
        if config_guild:
            guild, is_guild_created = Guild.objects.get_or_create(
                name=config_guild["name"],
                description=config_guild["description"]
            )
        else:
            guild = None

        Player.objects.create(
            nickname=player_name,
            email=player_info["email"],
            bio=player_info["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
