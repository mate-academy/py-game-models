import json
from db.models import Race, Skill, Guild, Player


def main() -> None:
    with open("players.json", "r") as file:
        players_data = json.load(file)

    for player_data in players_data:
        race, _ = Race.objects.get_or_create(
            name=player_data["race"]["name"],
            defaults={"description": player_data["race"]["description"]},
        )

        skills = []
        for skill_data in player_data["race"]["skills"]:
            skill, _ = Skill.objects.get_or_create(
                name=skill_data["name"],
                defaults={"bonus": skill_data["bonus"], "race": race},
            )
            skills.append(skill)

        guild = None
        if "guild" in player_data:
            guild, _ = Guild.objects.get_or_create(
                name=player_data["guild"]["name"],
                defaults={"description": player_data["guild"]["description"]},
            )

        Player.objects.get_or_create(
            nickname=player_data["nickname"],
            defaults={
                "email": player_data["email"],
                "bio": player_data["bio"],
                "race": race,
                "guild": guild,
            },
        )
