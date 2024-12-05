import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_file:
        players = json.load(players_file)

    for player_nickname, player in players.items():
        race_data = player.get("race")
        race, _ = Race.objects.get_or_create(
            name=race_data.get("name"),
            description=race_data.get("description")
        )

        guild_data = player.get("guild")
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data.get("name"),
                description=guild_data.get("description")
            )
        else:
            guild = None

        for skill_data in race_data.get("skills", []):
            skill, _ = Skill.objects.get_or_create(
                name=skill_data.get("name"),
                bonus=skill_data.get("bonus"),
                race=race
            )

        Player.objects.get_or_create(
            nickname=player_nickname,
            email=player.get("email"),
            bio=player.get("bio"),
            race=race,
            guild=guild,
            created_at=player.get("created_at")
        )


if __name__ == "__main__":
    main()
