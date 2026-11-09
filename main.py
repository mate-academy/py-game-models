import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild
import json


def main() -> None:
    with open("players.json", "r") as file:
        players_dic: dict = json.load(file)

    for player, player_value in players_dic.items():

        race_value = player_value["race"]
        player_race, _ = Race.objects.get_or_create(
            name=race_value["name"],
            description=race_value["description"]
        )

        if len(race_value["skills"]) > 0:
            race_skils = race_value["skills"]
            for skill in race_skils:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=player_race
                )

        guild = player_value.get("guild")

        if guild:
            player_guild, _ = Guild.objects.get_or_create(
                name=guild["name"],
                description=guild["description"]
            )
        else:
            player_guild = None

        Player.objects.get_or_create(
            nickname=player,
            email=player_value["email"],
            bio=player_value["bio"],
            race=player_race,
            guild=player_guild
        )


if __name__ == "__main__":
    main()
