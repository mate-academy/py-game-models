import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)
    for nickname, player in data.items():
        race_data = player["race"]
        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            description=race_data.get("description", "")
        )
        guild_data = player.get("guild")
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                description=guild_data.get("description", "")
            )
        else:
            guild = None
        for skill_info in race_data.get("skills", []):
            skill, _ = Skill.objects.get_or_create(
                name=skill_info["name"],
                bonus=skill_info.get("bonus", ""),
                race=race
            )
        player_obj, _ = Player.objects.get_or_create(
            nickname=nickname,
            email=player["email"],
            bio=player["bio"],
            race=race,
            guild=guild)


if __name__ == "__main__":
    main()
