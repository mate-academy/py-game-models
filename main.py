import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for player_key, player_value in players.items():
        guild_obj = None
        race_obj, _ = Race.objects.get_or_create(
            name=player_value.get("race").get("name"),
            description=player_value.get("race").get("description", "")
        )

        skills = player_value.get("race").get("skills")
        for skill in skills:
            skill_obj, _ = Skill.objects.get_or_create(
                name=skill.get("name"),
                bonus=skill.get("bonus"),
                race=race_obj)

        if player_value.get("guild"):
            guild_obj, _ = Guild.objects.get_or_create(
                name=player_value.get("guild").get("name"),
                description=player_value.get("guild").get("description")
            )

        player_obj, _ = Player.objects.get_or_create(
            nickname=player_key,
            email=player_value.get("email"),
            bio=player_value.get("bio"),
            race=race_obj,
            guild=guild_obj
        )


if __name__ == "__main__":
    main()
