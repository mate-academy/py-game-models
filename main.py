import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as data_file:
        data = json.load(data_file)
    for player in data:
        race_data = data[player]["race"]
        Race.objects.get_or_create(
            name=race_data["name"],
            description=race_data["description"]
        )
        race = Race.objects.get(name=race_data["name"])

        for skill in race_data["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race_id=race.id
            )

        guild_data = data[player]["guild"] if data[player]["guild"] else None
        if guild_data:
            Guild.objects.get_or_create(
                name=guild_data["name"],
                description=guild_data["description"]
            )
            guild = Guild.objects.get(name=guild_data["name"])

            Player.objects.get_or_create(
                nickname=player,
                email=data[player]["email"],
                bio=data[player]["bio"],
                race_id=race.id,
                guild_id=guild.id
            )
        else:
            Player.objects.get_or_create(
                nickname=player,
                email=data[player]["email"],
                bio=data[player]["bio"],
                race_id=race.id,
            )


if __name__ == "__main__":
    main()
