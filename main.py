import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    Player.objects.all().delete()
    Race.objects.all().delete()
    Skill.objects.all().delete()
    Guild.objects.all().delete()

    with open("players.json") as f:
        data = json.load(f)

    for username, pdata in data.items():

        race_data = pdata.get("race")
        race_obj, _ = Race.objects.get_or_create(
            name=race_data.get("name", None),
            defaults={"description": race_data.get("description", None)}
        )

        skill_objs = []
        for skill in race_data.get("skills", []):
            skill_obj, _ = Skill.objects.get_or_create(
                name=skill.get("name", None),
                defaults={"bonus": skill.get("bonus", None), "race": race_obj}
            )
            skill_objs.append(skill_obj)

        guild_data = pdata.get("guild")
        guild_obj = None
        if guild_data:
            guild_obj, _ = Guild.objects.get_or_create(
                name=guild_data.get("name", None),
                defaults={"description": guild_data.get("description") or None}
            )

        player_obj, _ = Player.objects.get_or_create(
            nickname=username,
            defaults={
                "email": pdata.get("email", None),
                "bio": pdata.get("bio", ""),
                "race": race_obj,
                "guild": guild_obj
            }
        )


if __name__ == "__main__":
    main()
