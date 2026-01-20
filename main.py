import init_django_orm  # noqa: F401
import json


from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players_data = json.load(file)

    for player_name, player_data in players_data.items():
        guild_data = player_data.get("guild")
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                description=guild_data.get("description", "")
            )
        else:
            guild = None

        race_data = player_data.get("race")
        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            description=race_data.get("description", "")
        )

        skills_data = race_data.get("skills", [])
        for skill_data in skills_data:
            skill, _ = Skill.objects.get_or_create(
                name=skill_data["name"],
                bonus=skill_data.get("bonus", ""),
                race=race
            )

        Player.objects.get_or_create(
            nickname=player_name,
            email=player_data.get("email", ""),
            bio=player_data.get("bio", ""),
            guild=guild,
            race=race
        )


if __name__ == "__main__":
    main()
