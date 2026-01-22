import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_file:
        players = json.load(players_file)

    for name, config in players.items():
        race_cfg = config.get("race")
        race, _ = Race.objects.get_or_create(
            name=race_cfg.get("name"),
            defaults={"description": race_cfg.get("description")}
        )

        skills_cfg = race_cfg.get("skills", [])
        for skill in skills_cfg:
            Skill.objects.get_or_create(
                name=skill.get("name"),
                defaults={
                    "bonus": skill.get("bonus"),
                    "race": race
                }
            )

        guild_cfg = config.get("guild")
        guild = None
        if guild_cfg:
            guild, _ = Guild.objects.get_or_create(
                name=guild_cfg.get("name"),
                defaults={"description": guild_cfg.get("description")}
            )

        Player.objects.get_or_create(
            nickname=name,
            defaults={
                "email": config.get("email"),
                "bio": config.get("bio"),
                "race": race,
                "guild": guild
            }
        )


if __name__ == "__main__":
    main()
