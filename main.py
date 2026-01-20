import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for nickname, data in players.items():
        race_data = data["race"]
        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data["description"]})

        for skill in race_data.get("skills", []):
            Skill.objects.get_or_create(
                name=skill["name"],
                defaults={"bonus": skill["bonus"],
                          "race": race})

        guild = None
        if data.get("guild"):
            guild_data = data["guild"]
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data["description"]})

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={"email": data["email"],
                      "bio": data["bio"],
                      "race": race,
                      "guild": guild
                      })


if __name__ == "__main__":
    main()
