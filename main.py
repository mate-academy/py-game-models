import json
import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as field:
        config = json.load(field)

        for player_name, player_info in config.items():
            race, created_bool = Race.objects.get_or_create(
                name=player_info["race"]["name"],
                defaults={"description": player_info["race"]
                          ["description"]},
            )

            for skill in player_info["race"]["skills"]:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    defaults={"bonus": skill["bonus"], "race": race}
                )

            if player_info["guild"] is not None:
                guild, created_bool = Guild.objects.get_or_create(
                    name=player_info["guild"]["name"],
                    defaults={"description": player_info["guild"]
                              ["description"]},)
            else:
                guild = None

            Player.objects.create(
                nickname=player_name,
                email=player_info["email"],
                bio=player_info["bio"],
                race=race,
                guild=guild,

            )


if __name__ == "__main__":
    main()
