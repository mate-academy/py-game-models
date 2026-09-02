import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for name, player in players.items():
        guild = None
        race = None

        if player.get("race"):
            race_data = player["race"]
            race, _ = Race.objects.get_or_create(
                name=race_data["name"],
                defaults={"description": race_data["description"]}
            )

            if player["race"].get("skills"):
                skills_data = player["race"]["skills"]
                for skill_item in skills_data:
                    skill, _ = Skill.objects.get_or_create(
                        name=skill_item["name"],
                        defaults={
                            "bonus": skill_item["bonus"],
                            "race": race
                        }
                    )

        if player.get("guild"):
            guild_data = player["guild"]
            guild, _ = Guild.objects.get_or_create(
                name=player["guild"]["name"],
                defaults={"description": guild_data["description"]}
            )

        Player.objects.get_or_create(
            nickname=name,
            defaults={
                "email": player["email"],
                "bio": player["bio"],
                "race": race,
                "guild": guild,
            }
        )


if __name__ == "__main__":
    main()
