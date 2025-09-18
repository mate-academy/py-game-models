import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players = json.load(file)

    for key, info in players.items():
        player_name = key
        player_email = info.get("email")
        player_bio = info.get("bio")
        player_guild = info.get("guild")
        race = info.get("race")
        race_obj = None
        guild_object = None
        skills = (race or {}).get("skills")
        if race:
            race_obj, _ = Race.objects.get_or_create(
                name=race["name"],
                defaults={"description": race["description"]},
            )
            if skills:
                for skill in skills:
                    Skill.objects.get_or_create(
                        name=skill["name"],
                        defaults={
                            "bonus": skill["bonus"],
                            "race": race_obj}
                    )
        if player_guild:
            guild_object, _ = Guild.objects.get_or_create(
                name=player_guild["name"],
                defaults={"description": player_guild["description"]}
            )
        if race_obj:
            Player.objects.create(
                nickname=player_name,
                email=player_email,
                bio=player_bio,
                race=race_obj,
                guild=guild_object
                if player_guild else None
            )


if __name__ == "__main__":
    main()
