import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    created_races = 0
    created_skills = 0
    created_guilds = 0
    created_players = 0

    for nickname, info in data.items():
        race_data = info["race"]
        race, race_created = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data["description"]})
        if race_created:
            created_races += 1

        for skill_data in race_data["skills"]:
            skill, skill_created = Skill.objects.get_or_create(
                name=skill_data["name"],
                defaults={
                    "bonus": skill_data["bonus"],
                    "race": race
                }
            )
            if skill_created:
                created_skills += 1

        if info["guild"] is not None:
            guild_data = info["guild"]
            guild, guild_created = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data["description"]}
            )
            if guild_created:
                created_guilds += 1
        else:
            guild = None

        player, player_created = Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": info["email"],
                "bio": info["bio"],
                "race": race,
                "guild": guild
            }
        )
        if player_created:
            created_players += 1

    print(f"Players created: {created_players}")
    print(f"Races created: {created_races}")
    print(f"Skills created: {created_skills}")
    print(f"Guilds created: {created_guilds}")


if __name__ == "__main__":
    main()
