import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file_json:
        info = json.load(file_json)
        for nickname in info:

            if Race.objects.filter(
                    name=info[nickname]["race"]["name"],
                    description=info[nickname]["race"]["description"]
            ).exists() is False:
                Race.objects.create(
                    name=info[nickname]["race"]["name"],
                    description=info[nickname]["race"]["description"]
                )

            if not info[nickname]["guild"]:
                guild_name = None
            else:
                if Guild.objects.filter(
                    name=info[nickname]["guild"]["name"],
                    description=info[nickname]["guild"]["description"]
                ).exists() is False:
                    guild_name = Guild.objects.create(
                        name=info[nickname]["guild"]["name"],
                        description=info[nickname]["guild"]["description"]
                    )

            for single_skill in info[nickname]["race"]["skills"]:
                if Skill.objects.filter(
                    name=single_skill["name"],
                        bonus=single_skill["bonus"]
                ).exists() is False:
                    Skill.objects.create(
                        name=single_skill["name"],
                        bonus=single_skill["bonus"],
                        race=Race.objects.get(
                            name=info[nickname]["race"]["name"]
                        )
                    )
            Player.objects.create(
                    nickname=nickname,
                    email=info[nickname]["email"],
                    bio=info[nickname]["bio"],
                    race=Race.objects.get(
                        name=info[nickname]["race"]["name"]
                    ),
                    guild=None if not guild_name else Guild.objects.get(
                        name=info[nickname]["guild"]["name"]
                    )
                )


if __name__ == "__main__":
    main()
