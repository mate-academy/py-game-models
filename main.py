import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_json:
        players_data = json.load(players_json)

    for user, user_object in players_data.items():
        race = user_object.get("race")
        guild = user_object.get("guild")
        skills = race.get("skills")
        race_object, _ = Race.objects.get_or_create(
            name=race.get("name"),
            description=race.get("description")
        )

        guild_object_created = Guild.objects.get_or_create(
            name=guild.get("name"),
            description=guild.get("description")
        ) if guild else None

        for skill in skills:
            Skill.objects.get_or_create(
                name=skill.get("name"),
                bonus=skill.get("bonus"),
                race=race_object
            )

        Player.objects.get_or_create(
            nickname=user,
            email=user_object.get("email"),
            bio=user_object.get("bio"),
            race=race_object,
            guild=guild_object_created[0] if guild_object_created else None
        )
