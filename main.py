import init_django_orm  # noqa: F401
import os
import json

from db.models import Race, Skill, Player, Guild

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def main() -> None:
    with open(os.path.join(BASE_DIR, "db/tests/players.json")) as players:
        list_of_items = json.load(players)

        for nickname_, player_dict in list_of_items.items():
            email_ = player_dict["email"]
            bio_ = player_dict["bio"]

            if player_dict["guild"]:
                Guild.objects.get_or_create(**player_dict["guild"])
                guild_ = Guild.objects.get(**player_dict["guild"])
            else:
                guild_ = None

            Race.objects.get_or_create(
                name=player_dict["race"]["name"],
                description=player_dict["race"]["description"]
            )

            race_ = Race.objects.get(
                name=player_dict["race"]["name"],
                description=player_dict["race"]["description"]
            )

            for skill in player_dict["race"]["skills"]:
                Skill.objects.get_or_create(**skill, race=race_)

            Player.objects.get_or_create(
                nickname=nickname_,
                email=email_,
                bio=bio_,
                race=race_,
                guild=guild_
            )


if __name__ == "__main__":
    main()
