import init_django_orm  # noqa: F401

from json import load
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_info:
        players_data = load(players_info)

    for player, player_info in players_data.items():
        race_info = player_info.get("race")
        guild_info = player_info.get("guild")
        skills_info = race_info.get("skills") if race_info else None

        race = None

        if race_info:
            race, _ = Race.objects.get_or_create(
                name=race_info["name"],
                description=race_info["description"]
            )

        guild = None

        if guild_info:
            guild, _ = Guild.objects.get_or_create(
                name=guild_info["name"],
                description=guild_info["description"]
            )

        if race:
            user, _ = Player.objects.get_or_create(
                nickname=player,
                email=player_info["email"],
                bio=player_info["bio"],
                race=race,
                guild=guild
            )
            if skills_info:
                for skill in skills_info:
                    Skill.objects.get_or_create(
                        name=skill["name"],
                        bonus=skill["bonus"],
                        race=race
                    )


if __name__ == "__main__":
    main()
