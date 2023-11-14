import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players_info = json.load(file)

        for name, player in players_info.items():
            race = player.get("race")
            guild = player.get("guild")
            skills = race.get("skills")

            if race:
                race, _ = Race.objects.get_or_create(
                    name=race.get("name"),
                    description=race.get("description")
                )

            if skills:
                for skill in skills:
                    skill, _ = Skill.objects.get_or_create(
                        name=skill.get("name"),
                        bonus=skill.get("bonus"),
                        race=race
                    )

            if guild:
                guild, _ = Guild.objects.get_or_create(
                    name=guild.get("name"),
                    description=guild.get("description")
                )

            Player.objects.get_or_create(
                nickname=name,
                email=player.get("email"),
                bio=player.get("bio"),
                race=race,
                guild=guild
            )


if __name__ == "__main__":
    main()
