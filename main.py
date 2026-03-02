import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for nickname, pdata in players.items():
        race_data = pdata.get("race", {})
        race_obj, _ = Race.objects.get_or_create(
            name=race_data.get("name"),
            defaults={"description": race_data.get("description", "")}
        )

        guild_data = pdata.get("guild")

        if not guild_data:
            guild_obj = None
        else:
            guild_obj, _ = Guild.objects.get_or_create(
                name=guild_data.get("name"),
                defaults={"description": guild_data.get("description")}
            )

        player_obj, created = Player.objects.get_or_create(
            nickname=nickname,
            defaults={"email": pdata.get("email", ""),
                      "bio": pdata.get("bio", ""),
                      "race": race_obj,
                      "guild": guild_obj, }
        )

        for sk in race_data.get("skills", []):
            skill_obj, _ = Skill.objects.get_or_create(name=sk.get("name"),
                                                       defaults={"bonus": sk.get("bonus", ""),
                                                                 "race": race_obj}
                                                                )


if __name__ == "__main__":
    main()
