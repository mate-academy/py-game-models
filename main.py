import json
from django.utils import timezone
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players_data = json.load(file)

    for player_name, player_data in players_data.items():
        race, _ = (Race.objects.get_or_create
                   (name=player_data["race"]["name"],
                    description=player_data["race"]["description"]))
        guild_data = player_data.get("guild")
        if guild_data:
            guild, _ = (Guild.objects.get_or_create
                        (name=guild_data["name"],
                         description=guild_data["description"]))
        else:
            guild = None

        player, created = Player.objects.get_or_create(
            nickname=player_name,
            defaults={
                "email": player_data["email"],
                "bio": player_data["bio"],
                "race": race,
                "guild": guild,
                "created_at": timezone.now()
            }
        )

        for skill_data in player_data["race"]["skills"]:
            skill, _ = Skill.objects.get_or_create(
                name=skill_data["name"],
                bonus=skill_data["bonus"],
                race=race
            )


if __name__ == "__main__":
    main()
