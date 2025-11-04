import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        file_player = json.load(f)
    for nickname, players_info in file_player.items():
        race, _ = Race.objects.get_or_create(
            name=players_info["race"]["name"],
            defaults={"description": players_info["race"]["description"]}
        )

        for skill in players_info["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                race=race,
                defaults={"bonus": skill["bonus"]}
            )

        guild_data = players_info.get("guild")
        guild = None
        if guild_data is not None:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data["description"]}
            )

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": players_info["email"],
                "bio": players_info["bio"],
                "race": race,
                "guild": guild
            }
        )


if __name__ == "__main__":
    main()
