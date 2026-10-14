import json
import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        players_data = json.load(f)

    for nickname, player_data in players_data.items():
        player_data["nickname"] = nickname
        race_data = player_data.pop("race")
        guild_data = player_data.pop("guild", None)
        skills_data = player_data.pop("skills", [])
        race, _ = Race.objects.get_or_create(name=race_data)
        guild = None
        if guild_data:
            guild, _ = Guild.objects.get_or_create(name=guild_data)
        Player.objects.create(race=race, guild=guild, **player_data)
        for skill_data in skills_data:
            Skill.objects.get_or_create(
                name=skill_data["name"],
                bonus=skill_data["bonus"],
                race=race
            )


if __name__ == "__main__":
    main()
