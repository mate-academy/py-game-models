import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    for name, player_data in data.items():
        race_data = player_data.get("race")

        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data.get("description", "")}
        )
        guild = None
        if player_data.get("guild"):
            guild_data = player_data["guild"]
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data.get("description", "")}
            )
        player, _ = Player.objects.get_or_create(
            nickname=name,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race,
            guild=guild
        )

        for skill_data in race_data.get("skills", []):  # skills - список, а не словник
            Skill.objects.get_or_create(
                name=skill_data["name"],
                bonus=skill_data["bonus"],
                race=race
            )
if __name__ == "__main__":
    main()
