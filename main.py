import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild
import json


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for player, player_characters in players.items():

        race_name, _ = Race.objects.get_or_create(
            name=player_characters["race"]["name"],
            description=player_characters["race"]["description"]
        )

        for skill in player_characters["race"]["skills"]:
            if Skill.objects.filter(name=skill["name"]).exists() is False:
                Skill.objects.create(name=skill["name"],
                                     bonus=skill["bonus"], race=race_name)

        if player_characters["guild"] is not None:
            guild, _ = Guild.objects.get_or_create(
                name=player_characters["guild"]["name"],
                description=player_characters["guild"]["description"]
            )
        else:
            guild = None

        Player.objects.create(nickname=player,
                              email=player_characters["email"],
                              bio=player_characters["bio"],
                              race=race_name,
                              guild=guild)


if __name__ == "__main__":
    main()
