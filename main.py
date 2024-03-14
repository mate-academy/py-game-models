import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as config_file:
        players = json.load(config_file)
        for player, config in players.items():

            race, _ = Race.objects.get_or_create(
                name=config.get("race").get("name"),
                description=config.get("race").get("description")
            )

            for skill in config.get("race").get("skills"):
                Skill.objects.get_or_create(
                    name=skill.get("name"),
                    bonus=skill.get("bonus"),
                    race=race
                )

            guild = None
            if config.get("guild"):
                guild, _ = Guild.objects.get_or_create(
                    name=config.get("guild").get("name"),
                    description=config.get("guild").get("description")
                )

            Player.objects.get_or_create(
                nickname=player,
                email=config.get("email"),
                bio=config.get("bio"),
                race=race,
                guild=guild
            )


if __name__ == "__main__":
    main()
