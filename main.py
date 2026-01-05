import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        data = json.load(file)
    for name, player in data.items():

        race_data = player.get("race")
        race_obj = None
        if race_data is not None:
            race_obj, _ = Race.objects.get_or_create(
                name=race_data.get("name"),
                defaults={"description": race_data.get("description")}
            )

            for skill in race_data.get("skills", []):
                skill_obj, _ = Skill.objects.get_or_create(
                    name=skill.get("name"),
                    defaults={"bonus": skill.get("bonus"), "race": race_obj})

        guild_data = player.get("guild")
        guild_obj = None
        if guild_data is not None:
            guild_obj, _ = Guild.objects.get_or_create(
                name=guild_data.get("name"),
                defaults={"description": guild_data.get("description")}
            )
        player_obj, _ = Player.objects.get_or_create(
            nickname=name,
            defaults={"email": player.get("email"),
                      "bio": player.get("bio"),
                      "race": race_obj,
                      "guild": guild_obj
                      }
        )


if __name__ == "__main__":
    main()
