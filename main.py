import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as config_file:
        players = json.load(config_file)
        for player, config in players.items():

            race, _ = Race.objects.get_or_create(
                name=config["race"]["name"],
                description=config["race"]["description"]
            )

            for skill in config["race"]["skills"]:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )

            guild = None
            if config.get("guild"):
                guild, _ = Guild.objects.get_or_create(
                    name=config["guild"]["name"],
                    description=config["guild"]["description"]
                )

            Player.objects.get_or_create(
                nickname=player,
                email=config["email"],
                bio=config["bio"],
                race=race,
                guild=guild
            )


if __name__ == "__main__":
    main()
