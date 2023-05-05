import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players = json.load(file)

    for player_name, player_data in players.items():
        player_guild = player_data.get("guild")
        player_race_name = player_data.get("race", {}).get("name")
        player_race_description = player_data.get("race", {}).get("description")
        player_skills = player_data.get("race", {}).get("skills")

        guild = None
        if player_guild is not None:
            guild, _ = Guild.objects.get_or_create(
                name=player_guild.get("name"),
                defaults={
                    "description": player_guild.get("description")
                }
            )

        if not player_race_description:
            player_race_description = ""
        race, _ = Race.objects.get_or_create(
            name=player_race_name,
            defaults={
                "description": player_race_description
            }
        )

        for skill in player_skills:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                defaults={"race": race}
            )

        Player.objects.create(
            nickname=player_name,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
