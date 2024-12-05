import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for nickname, player_data in data.items():
        guild_dict = player_data["guild"]
        guild = None
        if guild_dict:
            guild, is_guild_created = Guild.objects.get_or_create(
                name=guild_dict["name"],
                description=guild_dict["description"]
            )

        race_dict = player_data["race"]
        race, is_race_created = Race.objects.get_or_create(
            name=race_dict["name"],
            description=race_dict["description"]
        )

        for skill in race_dict["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )

        Player.objects.create(
            nickname=nickname,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
