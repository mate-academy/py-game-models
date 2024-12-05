import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    Race.objects.all().delete()

    with open("players.json", "r") as file:
        players_data = json.load(file)

    for player_nickname, all_info in players_data.items():
        nickname = player_nickname
        e_mail = all_info.get("email")
        bio = all_info.get("bio")
        guild_object = None

        race_name = all_info.get("race").get("name")
        race_description = all_info.get("race").get("description")
        race_object, created = Race.objects.get_or_create(
            name=race_name, description=race_description
        )

        skills = all_info.get("race").get("skills")
        if skills:
            for skill_info in skills:
                skill_name = skill_info.get("name")
                skill_bonus = skill_info.get("bonus")
                Skill.objects.get_or_create(
                    name=skill_name, bonus=skill_bonus, race=race_object
                )

        if all_info.get("guild"):
            guild_name = all_info.get("guild").get("name")
            guild_description = all_info.get("guild").get("description")
            guild_object, created = Guild.objects.get_or_create(
                name=guild_name, description=guild_description
            )

        Player.objects.create(
            nickname=nickname,
            email=e_mail,
            bio=bio,
            race=race_object,
            guild=guild_object,
        )


if __name__ == "__main__":
    main()
