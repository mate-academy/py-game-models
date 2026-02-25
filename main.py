import init_django_orm  # noqa: F401
import json


from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)
    for player, player_info in players.items():
        email = player_info.get("email")
        bio = player_info.get("bio")
        guild = player_info.get("guild")
        race = player_info.get("race")

        guild_obj = None
        race_obj = None

        if guild:
            guild_obj, _ = Guild.objects.get_or_create(
                name=guild.get("name"), description=guild.get("description")
            )
        if race:
            race_skills = race.get("skills", [])
            race_name = race.get("name")
            race_description = race.get("description")
            race_obj, _ = Race.objects.get_or_create(
                name=race_name, description=race_description
            )
            for skill in race_skills:
                skill_name = skill.get("name")
                skill_bonus = skill.get("bonus")
                Skill.objects.get_or_create(
                    name=skill_name, bonus=skill_bonus, race=race_obj
                )

        Player.objects.get_or_create(
            email=email,
            bio=bio,
            guild=guild_obj,
            race=race_obj,
            nickname=player
        )


if __name__ == "__main__":
    main()
