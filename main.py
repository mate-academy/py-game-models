import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for nickname, value in data.items():
        obj_race, _ = Race.objects.get_or_create(
            name=value.get("race", {}).get("name"),
            description=value.get("race", {}).get("description")
        )

        for skills in value.get("race", {}).get("skills"):
            Skill.objects.get_or_create(
                name=skills.get("name"),
                bonus=skills.get("bonus"),
                race=obj_race
            )

        guild_data = value.get("guild")
        if guild_data:
            obj_guild, _ = Guild.objects.get_or_create(
                name=guild_data.get("name"),
                description=guild_data.get("description")
            )
        else:
            obj_guild = None

        Player(
            nickname=nickname,
            email=value.get("email"),
            bio=value.get("bio"),
            race=obj_race,
            guild=obj_guild,
        ).save()


if __name__ == "__main__":
    main()
