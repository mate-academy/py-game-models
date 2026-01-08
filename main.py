import json
import init_django_orm  # noqa: F401
from django.db.models import QuerySet

from db.models import Race, Skill, Player, Guild


def main() -> None:
    races: QuerySet[Race] = Race.objects
    skills: QuerySet[Skill] = Skill.objects
    guilds: QuerySet[Guild] = Guild.objects
    players_qs: QuerySet[Player] = Player.objects

    with open("players.json", "r") as file:
        players_data = json.load(file)

    for name, player_data in players_data.items():
        guild = player_data.get("guild")
        guild_data = None

        if guild:
            guild_data, _ = guilds.get_or_create(
                name=guild.get("name"),
                defaults={"description": guild.get("description", None)}
            )

        race = player_data.get("race")

        race_data, _ = races.get_or_create(
            name=race.get("name"),
            defaults={"description": race.get("description", "")}
        )

        for skill in race.get("skills", []):
            skills.get_or_create(
                name=skill.get("name"),
                bonus=skill.get("bonus"),
                race=race_data
            )

        players_qs.create(
            nickname=name,
            email=player_data.get("email"),
            bio=player_data.get("bio"),
            race=race_data,
            guild=guild_data,
        )


if __name__ == "__main__":
    main()
