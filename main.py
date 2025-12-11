import json
import init_django_orm  # noqa: F401


from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as data_file:
        players = json.load(data_file)

    for nickname, data in players.items():
        guild_obj = None
        guild_data = data.get("guild")

        if guild_data:
            guild_obj, _ = Guild.objects.get_or_create(
                name=guild_data.get("name"),
                defaults={"description": guild_data.get("description")}
            )

        race_data = data.get("race")
        if race_data:  # ← ИСПРАВЛЕНО: добавлена проверка
            race_obj, _ = Race.objects.get_or_create(
                name=race_data.get("name"),
                defaults={"description": race_data.get("description")}
            )

            for skill in race_data.get("skills", []):
                Skill.objects.get_or_create(
                    name=skill.get("name"),
                    race=race_obj,
                    defaults={"bonus": skill.get("bonus")}
                )

            Player.objects.get_or_create(
                nickname=nickname,
                defaults={
                    "email": data.get("email"),
                    "bio": data.get("bio"),
                    "race": race_obj,
                    "guild": guild_obj
                }
            )


if __name__ == "__main__":
    main()
