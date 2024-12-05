import init_django_orm  # noqa: F401
import json


from db.models import Race, Skill, Guild, Player


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for nickname, player_data in players.items():
        race_data = player_data.get("race")
        race, _ = Race.objects.get_or_create(
            name=race_data.get("name"),
            description=race_data.get("description")
        )

        skills_data = race_data.get("skills", [])
        for skill in skills_data:
            Skill.objects.get_or_create(name=skill.get("name"),
                                        bonus=skill.get("bonus"),
                                        race=race)

        guild_data = player_data.get("guild")
        guild = None
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data.get("name"),
                description=guild_data.get("description", None)
            )

        Player.objects.create(nickname=nickname,
                              email=player_data.get("email"),
                              bio=player_data.get("bio"),
                              race=race,
                              guild=guild)


if __name__ == "__main__":
    main()
