from email.policy import default
import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_file:
        players_data = json.load(players_file)

    for nickname, player in players_data.items():
        race_data = player["race"]
        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data["description"],}
        )

        guild = None
        if player.get("guild"):
            guild_data = player["guild"]
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data.get("description", None)}
            )

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": player["email"],
                "bio": player["bio"],
                "race": race,
                "guild": guild
            }
        )

        for skill_data in race_data.get("skills", []):
            Skill.objects.get_or_create(
                name=skill_data["name"],
                race=race,
                defaults={"bonus": skill_data["bonus"]}
            )


if __name__ == "__main__":
    main()
