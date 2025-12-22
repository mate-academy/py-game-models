import json
import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        players = json.load(f)
    for nickname, player_data in players.items():
        email = player_data["email"]
        bio = player_data["bio"]
        race_data = player_data["race"]
        guild_data = player_data["guild"]

        race, created = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data["description"]},
        )

        for skill_data in race_data.get("skills", []):
            skill, created = Skill.objects.get_or_create(
                name=skill_data["name"],
                defaults={"bonus": skill_data["bonus"],
                          "race": race})

        guild = None
        if guild_data:
            guild, created = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data["description"]}
            )

        player, created = Player.objects.get_or_create(
            nickname=nickname,
            defaults={"email": email,
                      "bio": bio,
                      "race": race,
                      "guild": guild})


if __name__ == "__main__":
    main()
