import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players_data = json.load(file)

    for nickname, player in players_data.items():
        race_dict = player.get("race")
        race_obj, _ = Race.objects.get_or_create(
            name=race_dict.get("name"),
            defaults={"description": race_dict.get("description")}
        )

        for skill_dict in race_dict.get("skills"):
            Skill.objects.get_or_create(
                name=skill_dict.get("name"),
                defaults={
                    "bonus": skill_dict.get("bonus"),
                    "race": race_obj
                }
            )

        guild_dict = player.get("guild")
        if guild_dict:
            guild_obj, _ = Guild.objects.get_or_create(
                name=guild_dict.get("name"),
                defaults={"description": guild_dict.get("description")}
            )
        else:
            guild_obj = None

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": player.get("email"),
                "bio": player.get("bio"),
                "race": race_obj,
                "guild": guild_obj,
            }
        )


if __name__ == "__main__":
    main()
