import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for nickname, value in data.items():
        race_data = value.get("race", {})
        obj_race, _ = Race.objects.get_or_create(
            name=race_data.get("name"),
            description=race_data.get("description")
        )

        for skill in race_data.get("skills", []):
            Skill.objects.get_or_create(
                name=skill.get("name"),
                bonus=skill.get("bonus"),
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

        obj_player, _ = Player.objects.get_or_create(
            nickname=nickname,
            email=value.get("email"),
            bio=value.get("bio"),
            race=obj_race,
            guild=obj_guild,
        )


if __name__ == "__main__":
    main()
