import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r", encoding="utf-8") as file:
        players = json.load(file)

    for nickname, player_info in players.items():

        race, race_created = Race.objects.get_or_create(
            name=player_info["race"]["name"],
            defaults={"description" : player_info["race"].get(
                "description", ""
            )},
        )

        if "skills" in player_info["race"]:
            for skill_info in player_info["race"]["skills"]:
                Skill.objects.get_or_create(
                    name=skill_info["name"],
                    defaults={"bonus" : skill_info["bonus"], "race" : race},
                )

        guild = None
        if "guild" in player_info and player_info["guild"]:
            guild, guild_created = Guild.objects.get_or_create(
                name=player_info["guild"]["name"],
                defaults={"description" : player_info["guild"].get(
                    "description", None
                )},
            )

        player, player_created = Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email" : player_info["email"],
                "bio" : player_info.get("bio", ""),
                "race" : race,
                "guild" : guild
            }
        )


if __name__ == "__main__":
    main()
