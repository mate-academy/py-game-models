import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players_data = json.load(file)

    for player_nickname, player_data in players_data.items():
        race_data = player_data["race"]
        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            description=race_data.get("description")
        )

        guild_data = player_data.get("guild")
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data.get("name"),
                defaults={"description": guild_data.get("description", "")}
            )
        else:
            guild = None

        skills = []
        for skill_data in race_data.get("skills", []):
            skill, _ = Skill.objects.get_or_create(
                name=skill_data["name"],
                bonus=skill_data.get("bonus", ""),
                race=race
            )
            skills.append(skill)

        Player.objects.get_or_create(
            nickname=player_nickname,
            defaults={
                "email": player_data["email"],
                "bio": player_data["bio"],
                "race": race,
                "guild": guild,
                "created_at": player_data.get("created_at")
            }
        )


if __name__ == "__main__":
    main()
