import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file_out:
        data = json.load(file_out)

    for nickname, player_data in data.items():
        race_data = player_data.get("race")
        guild_data = player_data.get("guild")

        race = Race.objects.get_or_create(
            name=race_data["name"],
            description=race_data["description"],
        )[0]
        for skill in race_data.get("skills"):
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race,
            )
        if guild_data:
            guild = Guild.objects.get_or_create(
                name=guild_data["name"],
                description=guild_data["description"],
            )[0]
        else:
            guild = None
        Player.objects.create(
            nickname=nickname,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
