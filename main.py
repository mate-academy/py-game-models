import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for user, info in data.items():
        nickname = user
        email = info.get("email")
        bio = info.get("bio")

        if info["guild"]:
            guild_name = (info["guild"]["name"]
                          if info["guild"]["name"] else None)
            guild_description = (info["guild"]["description"]
                                 if info["guild"]["description"] else None)

            if not Guild.objects.filter(name=guild_name).exists():
                guild_link = Guild.objects.create(
                    name=guild_name,
                    description=guild_description
                )

        if info["race"]:
            race_name = info["race"]["name"] if info["race"]["name"] else None
            race_description = (info["race"]["description"]
                                if info["race"]["description"] else None)

            if not Race.objects.filter(name=race_name).exists():
                race_link = Race.objects.create(
                    name=race_name,
                    description=race_description
                )

            if info["race"]["skills"]:
                for skill in info["race"]["skills"]:
                    skill_name = skill.get("name")
                    skill_bonus = skill.get("bonus")

                    if not Skill.objects.filter(name=skill_name).exists():
                        Skill.objects.create(
                            name=skill_name,
                            bonus=skill_bonus,
                            race=race_link
                        )

        Player.objects.create(
            nickname=nickname,
            email=email,
            bio=bio,
            race=race_link if info["race"]["name"] else None,
            guild=guild_link if info.get("guild") else None
        )


if __name__ == "__main__":
    main()
