import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild
import json


def main() -> None:
    with open("players.json", "r") as file:
        players_data = json.load(file)

    for nickname in players_data:
        race_data = players_data[nickname]["race"]
        race, created = Race.objects.get_or_create(
            name=race_data["name"],
            description=race_data["description"]
        )
        guild_data = players_data[nickname]["guild"]
        if guild_data:
            description_data = guild_data["description"]\
                if guild_data["description"]\
                else None
            guild, created = Guild.objects.get_or_create(
                name=guild_data["name"],
                description=description_data
            )
        else:
            guild = None
        Player.objects.create(
            nickname=nickname,
            email=players_data[nickname]["email"],
            bio=players_data[nickname]["bio"],
            race=race,
            guild=guild
        )

        for skill in race_data["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )


if __name__ == "__main__":
    main()
