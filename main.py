import json
from app.models import Player, Guild, Race, Skill


def main():
    with open("players.json", "r") as file:
        players_data = json.load(file)

    for data in players_data:
        guild = None
        if data.get("guild"):
            guild, _ = Guild.objects.get_or_create(
                name=data["guild"]
            )

        race = None
        if data.get("race"):
            race, _ = Race.objects.get_or_create(
                name=data["race"]
            )

        player = Player.objects.create(
            nickname=data["nickname"],
            level=data["level"],
            guild=guild,
            race=race,
        )

        for skill_name in data.get("skills", []):
            skill, _ = Skill.objects.get_or_create(
                name=skill_name
            )
            player.skills.add(skill)


if __name__ == "__main__":
    main()
