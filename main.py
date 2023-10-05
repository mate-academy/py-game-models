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
        guild = None

        race_name = all_info.get("race").get("name")
        race_description = all_info.get("race").get("description")
        Race.objects.get_or_create(
            name=race_name, description=race_description
        )
        race_object = Race.objects.get(name=race_name)

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
            Guild.objects.get_or_create(
                name=guild_name, description=guild_description
            )
            guild = Guild.objects.get(
                name=guild_name, description=guild_description
            )

        Player.objects.create(
            nickname=nickname,
            email=e_mail,
            bio=bio,
            race=race_object,
            guild=guild,
        )


if __name__ == "__main__":
    main()
