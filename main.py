import init_django_orm  # noqa: F401


import json
import os.path


from db.models import Race, Skill, Player, Guild


def main() -> None:
    file_path = os.path.abspath("players.json")
    with open(file_path, mode="r") as file:
        players_data = json.load(file)

    for nickname, player_detail in players_data.items():

        race_detail = player_detail.get("race", {})
        race_name = race_detail.get("name")
        race_description = race_detail.get("description", "")

        race_obj, _ = Race.objects.get_or_create(
            name=race_name,
            defaults={"description": race_description}
        )

        skills_detail = race_detail.get("skills", [])

        for skill in skills_detail:
            name = skill.get("name")
            bonus = skill.get("bonus")

            Skill.objects.get_or_create(
                name=name,
                defaults={"race": race_obj, "bonus": bonus}
            )

        guild_detail = player_detail.get("guild")
        guild_obj = None

        if guild_detail and guild_detail.get("name"):
            guild_name = guild_detail.get("name")
            guild_description = guild_detail.get("description")

            guild_obj, _ = Guild.objects.get_or_create(
                name=guild_name,
                defaults={"description": guild_description}
            )

        email = player_detail.get("email")
        bio = player_detail.get("bio")

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": email,
                "bio": bio,
                "race": race_obj,
                "guild": guild_obj
            }
        )


if __name__ == "__main__":
    main()
