import json
from app.models import Player, Guild, Race, Skill


def main():
    with open("players.json", "r") as file:
        players_data = json.load(file)

    for data in players_data:
        # Guild
        guild = None
        if data.get("guild"):
            guild, _ = Guild.objects.get_or_create(
                name=data["guild"]
            )

        # Race (обов’язкова для Skill)
        race = None
        if data.get("race"):
            race, _ = Race.objects.get_or_create(
                name=data["race"]
            )

        # Player (тільки правильні поля)
        player = Player.objects.create(
            nickname=data["nickname"],
            email=data["email"],
            bio=data["bio"],
            guild=guild,
            race=race,
        )

        # Skills (прив’язка до Race, НЕ до Player)
        for skill_data in data.get("skills", []):
            Skill.objects.get_or_create(
                name=skill_data["name"],
                race=race,
                defaults={
                    "bonus": skill_data["bonus"]
                }
            )


if __name__ == "__main__":
    main()
