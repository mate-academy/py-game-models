import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for player_name, player_data in data.items():
        race, _ = Race.objects.get_or_create(
            name=player_data["race"]["name"],
            description=player_data["race"]["description"]
        )

        guild_data = player_data.get("guild")
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                description=guild_data.get("description", None)
            )
        else:
            guild = None

        player, _ = Player.objects.get_or_create(
            nickname=player_name,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race,
            guild=guild
        )

        for skill in player_data["race"]["skills"]:
            skill, _ = Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )
        player.save()


if __name__ == "__main__":
    main()
