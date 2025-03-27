import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_file:
        players_data = json.load(players_file)
    for player_nickname, player_info in players_data.items():
        email, bio, race_info, guild_info = player_info.values()

        race, _ = Race.objects.get_or_create(
            name=race_info["name"],
            description=race_info.get("description")
        )

        for skill_data in race_info.get("skills"):
            Skill.objects.get_or_create(
                name=skill_data["name"],
                bonus=skill_data["bonus"],
                race=race,
            )

        guild = None
        if guild_info:
            guild, _ = Guild.objects.get_or_create(**guild_info)

        player, _ = Player.objects.get_or_create(
            nickname=player_nickname,
            email=email,
            bio=bio,
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
