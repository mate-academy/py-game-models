import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players_info = json.load(file)

    for nickname, player_info in players_info.items():
        email = player_info.get("email")
        bio = player_info.get("bio")
        race_info = player_info.get("race")
        skills_info = race_info.get("skills")
        guild_info = player_info.get("guild")

        race = Race.objects.get_or_create(
            name=race_info.get("name"),
            description=race_info.get("description")
        )[0]

        for skill in skills_info:
            Skill.objects.get_or_create(
                name=skill.get("name"),
                bonus=skill.get("bonus"),
                race_id=race.id
            )

        if guild_info:
            guild = Guild.objects.get_or_create(
                name=guild_info.get("name"),
                description=guild_info.get("description")
            )[0]
        else:
            guild = None

        Player.objects.get_or_create(
            nickname=nickname,
            email=email,
            bio=bio,
            race_id=race.id,
            guild=guild
        )


if __name__ == "__main__":
    main()
