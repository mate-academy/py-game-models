import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:

    with open("players.json", "r") as data_file:
        data = json.load(data_file)

    for player_name, information in data.items():
        race_data = information.get("race")
        skills_data = information.get("race").get("skills")
        guild = information.get("guild")

        race, _ = Race.objects.get_or_create(
            name=race_data.get("name"),
            description=race_data.get("description")
        )

        for skill in skills_data:
            Skill.objects.get_or_create(
                name=skill.get("name"),
                bonus=skill.get("bonus"),
                race=race
            )

        if guild:
            guild, _ = Guild.objects.get_or_create(
                name=guild.get("name"),
                description=guild.get("description")
            )

        Player.objects.get_or_create(
            nickname=player_name,
            email=information.get("email"),
            bio=information.get("bio"),
            race=race,
            guild=guild
        )
