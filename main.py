import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_card_file:
        data_players = json.load(players_card_file)
        for nickname, player in data_players.items():

            # race
            race, created = Race.objects.get_or_create(
                name=player["race"]["name"],
                description=player["race"]["description"]
            )

            # skills
            for skills in player["race"]["skills"]:
                Skill.objects.get_or_create(
                    name=skills["name"],
                    bonus=skills["bonus"],
                    race=race
                )

            # guild
            guild = Guild.objects.get_or_create(
                name=player["guild"]["name"],
                description=player["guild"]["description"]
            )[0] if player["guild"] else None

            # player
            Player.objects.get_or_create(
                nickname=nickname,
                email=player["email"],
                bio=player["bio"],
                race=race,
                guild=guild,
            )


if __name__ == "__main__":
    main()
