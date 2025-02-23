import json
import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("file.json") as file:
        data_players = json.load(file)

    for player, data_player in data_players.items():
        player_race = data_player["race"]
        player_guild = data_player["guild"]
        player_skills = player_race["skills"]
        race = Race.objects.create(
            name=player_race["name"],
            defaults={"description": player_race["description"]}
        )
        if player_guild:
            guild = Guild.objects.get_or_create(
                name=player_guild["name"],
                defaults={"description": player_guild["description"]}
            )
        if player_skills:
            for skill_data in player_skills:
                skill_data = Skill.objects.create(
                    name=skill_data["name"],
                    bonus=skill_data["bonus"]
                )
        Player.objects.get_or_create(
            nickname=player,
            defaults={
                "email": data_player["email"],
                "bio": data_player["bio"],
                "race": race,
                "guild": guild
            }
        )


if __name__ == "__main__":
    main()
