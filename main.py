import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for nickname, data in players.items():

        race_name = data["race"]["name"]
        race_des = data["race"]["description"]
        race_object = Race.objects.get_or_create(
            name=race_name,
            description=race_des
        )[0]

        skills_list = data["race"].get("skills", [])
        for skill in skills_list:
            skill_name = skill["name"]
            skill_bonus = skill["bonus"]

            Skill.objects.get_or_create(
                name=skill_name,
                bonus=skill_bonus,
                race=race_object
            )

        guild_object = None
        if data.get("guild") is not None:
            guild_name = data["guild"]["name"]
            guild_des = data["guild"]["description"]
            guild_object = Guild.objects.get_or_create(
                name=guild_name, description=guild_des
            )[0]

        Player.objects.get_or_create(
            nickname=nickname,
            email=data.get("email"),
            bio=data.get("bio"),
            race=race_object,
            guild=guild_object,
        )


if __name__ == "__main__":
    main()
