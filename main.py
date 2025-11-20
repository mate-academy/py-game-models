import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Player, Guild


def load_player_data() -> dict[str, dict]:
    try:
        with open("players.json", "r") as file:
            return json.load(file)
    except FileNotFoundError as exc:
        raise SystemExit(f"File not found: {exc}")
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid JSON format: {exc}")


def main() -> None:
    player_data = load_player_data()

    for nickname, player_info in player_data.items():

        email = player_info.get("email", "Email not provided")
        bio = player_info.get("bio", "BIO not provided")

        guild_info = player_info.get("guild", {})
        guild = None
        if guild_info:
            guild, _ = Guild.objects.get_or_create(
                name=guild_info.get("name", "Unknown guild"),
                defaults={"description": guild_info.get("description")}
            )

        race_info = player_info.get("race", {})
        race, _ = Race.objects.get_or_create(
            name=race_info.get("name", "Unknown race"),
            defaults={"description": race_info.get("description")}
        )

        skills_info = race_info.get("skills", [])
        for skill_info in skills_info:
            Skill.objects.get_or_create(
                name=skill_info.get("name", "Unknown skill"),
                race=race,
                defaults={"bonus": skill_info.get("bonus", "")}
            )

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": email,
                "bio": bio,
                "race": race,
                "guild": guild
            }
        )


if __name__ == "__main__":
    main()
