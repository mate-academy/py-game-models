import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file_players:
        data_players = json.load(file_players)
    for player_name, player in data_players.items():
        data_guild = player.get("guild")
        if data_guild:
            guild, _ = Guild.objects.get_or_create(
                name=data_guild["name"],
                description=data_guild["description"]
            )
        else:
            guild = None
        date_race = player.get("race")
        race, _ = Race.objects.get_or_create(
            name=date_race["name"],
            description=date_race["description"]
        )
        for skill in date_race["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                defaults={"bonus": skill["bonus"]},
                race=race
            )
        data_email = player.get("email")
        data_bio = player.get("bio")
        Player.objects.create(
            nickname=player_name,
            email=data_email,
            bio=data_bio,
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
