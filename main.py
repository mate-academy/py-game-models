import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as json_file:
        players = json.load(json_file)

    for player, player_data in players.items():
        race = None
        if player_data.get("race"):
            race_name = player_data["race"]["name"]
            race_description = player_data["race"]["description"]
            race_skills = player_data["race"]["skills"]

            race, created = Race.objects.get_or_create(
                name=race_name,
                description=race_description
            )

            for skill in race_skills:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )

            race = Race.objects.get(name=race_name)

        guild = None
        if player_data.get("guild"):
            guild_name = player_data["guild"]["name"]
            guild_descr = player_data["guild"]["description"]

            guild, created = Guild.objects.get_or_create(
                name=guild_name,
                description=guild_descr
            )

        Player.objects.create(
            nickname=player,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
