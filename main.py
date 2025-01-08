import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as source:
        players_data = json.load(source)

    for p_name, p_info in players_data.items():
        p_race = Race.objects.get_or_create(
            name=p_info["race"]["name"],
            description=p_info["race"]["description"]
        )[0]

        skills = p_info["race"]["skills"]
        if skills:
            for skill in skills:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=p_race
                )

        player_guild_info = p_info.get("guild")
        p_guild = (
            Guild.objects.get_or_create(
                name=player_guild_info["name"],
                description=player_guild_info.get("description")
            )[0] if player_guild_info is not None else None
        )

        Player.objects.get_or_create(
            nickname=p_name,
            email=p_info["email"],
            bio=p_info["bio"],
            race=p_race,
            guild=p_guild
        )


if __name__ == "__main__":
    main()
