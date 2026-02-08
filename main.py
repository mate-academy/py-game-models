import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players = json.load(file)

    for player_name, player in players.items():
        race = player.get("race")
        race_obj = None
        if race:
            race_obj, created = Race.objects.get_or_create(
                name=race.get("name"),
                defaults={"description": race.get("description")}
            )
            for skill in race.get("skills", []):
                Skill.objects.get_or_create(
                    name=skill.get("name"),
                    defaults={
                        "bonus": skill.get("bonus"),
                        "race": race_obj
                    }
                )

        guild_obj = player.get("guild")
        if guild_obj:
            guild_obj, _ = Guild.objects.get_or_create(
                name=guild_obj.get("name"),
                defaults={"description": guild_obj.get("description")}
            )

        if None not in [player.get("email"), player.get("bio"), race_obj]:
            Player.objects.get_or_create(
                nickname=player_name,
                defaults={
                    "email": player.get("email"),
                    "bio": player.get("bio"),
                    "race": race_obj,
                    "guild": guild_obj
                }
            )


if __name__ == "__main__":
    main()
