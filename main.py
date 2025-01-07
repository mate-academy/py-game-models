import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:

    with open("players.json") as file:
        data = json.load(file)

    for nickname, player_data in data.items():
        race_data = player_data.get("race")
        race_model = None
        if race_data:
            race_model, _ = Race.objects.get_or_create(
                name=race_data.get("name"),
                defaults={"description": race_data.get("description")}
            )

        skills = race_data.get("skills", [])
        for skill_data in skills:
            Skill.objects.get_or_create(
                name=skill_data.get("name"),
                defaults={
                    "bonus": skill_data.get("bonus"),
                    "race": race_model
                }
            )

        guild_data = player_data.get("guild")
        guild_model = None
        if guild_data:
            guild_model, _ = Guild.objects.get_or_create(
                name=guild_data.get("name"),
                defaults={"description": guild_data.get("description")}
            )

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": player_data.get("email"),
                "bio": player_data.get("bio"),
                "race": race_model,
                "guild": guild_model
            }
        )


if __name__ == "__main__":
    main()
