import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as read_file:
        data = json.load(read_file)
        for nickname, detail_info in data.items():
            race = detail_info.get("race")
            new_race, _ = Race.objects.get_or_create(
                name=race.get("name"),
                description=race.get("description")
            )

            skills = race.get("skills")
            for skill in skills:
                Skill.objects.get_or_create(
                    race=new_race,
                    name=skill.get("name"),
                    bonus=skill.get("bonus")
                )

            guild = detail_info.get("guild")
            if guild:
                guild, _ = Guild.objects.get_or_create(
                    name=guild.get("name"),
                    description=guild.get("description")
                )

            Player.objects.get_or_create(
                nickname=nickname,
                email=detail_info.get("email"),
                bio=detail_info.get("bio"),
                race=new_race,
                guild=guild
            )


if __name__ == "__main__":
    main()
