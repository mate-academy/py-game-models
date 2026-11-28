import init_django_orm  # noqa: F401
from pathlib import Path
from json import load

from db.models import Race, Skill, Player, Guild


def main() -> None:
    config_path = Path(__file__).parent / "players.json"

    with config_path.open("r", encoding="utf-8") as file_in:
        json_data = load(file_in)

    for nickname, player_data in json_data.items():
        race, _ = Race.objects.get_or_create(
            name=player_data["race"]["name"],
            description=player_data["race"]["description"],
        )

        guild = player_data.get("guild")

        if guild:
            guild, _ = Guild.objects.get_or_create(
                name=player_data["guild"]["name"],
                defaults={
                    "description": player_data["guild"]["description"]
                }
            )

        Player.objects.create(
            nickname=nickname,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race,
            guild=guild,
        )

        for skill_data in player_data["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill_data["name"],
                bonus=skill_data["bonus"],
                race=race,
            )


if __name__ == "__main__":
    main()
