import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:

    with open("players.json", "r") as file_json:
        data_json = json.load(file_json)

    for player in data_json.keys():

        race_data = data_json[player].get("race")
        if race_data:
            race, _ = Race.objects.get_or_create(
                name=race_data.get("name"),
                description=race_data.get("description"),
            )

            for skills in race_data.get("skills"):
                Skill.objects.get_or_create(
                    name=skills.get("name"),
                    bonus=skills.get("bonus"),
                    race=race,
                )

        guild_data = data_json[player].get("guild")
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data.get("name"),
                description=guild_data.get("description"),
            )
        else:
            guild = guild_data

        Player.objects.create(
            nickname=player,
            email=data_json[player].get("email"),
            bio=data_json[player].get("bio"),
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
