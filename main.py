import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild
import json


def main() -> None:
    with open("players.json", "r") as players:
        data = json.load(players)
    for player, info in data.items():
        race = None
        race_data = info.get("race")
        if race_data:
            race, _ = Race.objects.get_or_create(
                name=race_data.get("name")
                , description=race_data.get("description"))
            for skill in race_data.get("skills"):
                Skill.objects.get_or_create(
                    name=skill.get("name"),
                    bonus=skill.get("bonus"),
                    race=race)
        guild_data = info.get("guild")
        guild = None
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data.get("name"),
                description=guild_data.get("description"))
        Player.objects.get_or_create(
            nickname=player,
            guild=guild, race=race,
            email=info.get("email"),
            bio=info.get("bio"))


if __name__ == "__main__":
    main()
