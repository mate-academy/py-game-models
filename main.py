import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as d:
        players_data = json.load(d)

    for nickname, p_data in players_data.items():
        race_data = p_data.get("race", {})
        race_name = race_data.get("name")
        race_description = race_data.get("description", "")
        race, _ = Race.objects.get_or_create(
            name=race_name,
            defaults={"description": race_description}
        )

        guild_data = p_data.get("guild")
        if guild_data:
            guild_name = guild_data.get("name")
            guild_description = guild_data.get("description")
            guild, _ = Guild.objects.get_or_create(
                name=guild_name,
                defaults={"description": guild_description}
            )
        else:
            guild = None

        for skill_data in race_data.get("skills", []):
            skill_name = skill_data.get("name")
            skill_bonus = skill_data.get("bonus", "")
            Skill.objects.get_or_create(
                name=skill_name,
                race=race,
                defaults={"bonus": skill_bonus}
            )

        email = p_data.get("email", "")
        bio = p_data.get("bio", "")
        Player.objects.create(
            nickname=nickname,
            email=email,
            bio=bio,
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
