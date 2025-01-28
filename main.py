import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    file_data = open("players.json")
    data = json.load(file_data)
    file_data.close()

    for player in data.keys():
        race, _ = Race.objects.get_or_create(
            name=data[player]["race"]["name"],
            description=data[player]["race"]["description"],
        )

        guild_data = data[player].get("guild")
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data.get("name", "Unknown Guild"),
                description=guild_data.get("description", ""),
            )
        else:
            guild = None  # Если данных о гильдии нет
        Player.objects.create(
            nickname=player,
            email=data[player]["email"],
            bio=data[player]["bio"],
            race=race,
            guild=guild
        )
        for skill in data[player]["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race,
            )


if __name__ == "__main__":
    main()
