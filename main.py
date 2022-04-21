import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main():
    with open("players.json", "r") as read_file:
        players_data = json.load(read_file)

    for player in players_data:
        nickname = player
        email = players_data[player]["email"]
        bio = players_data[player]["bio"]

        if not Race.objects.filter(
                name=players_data[player]["race"]["name"]
        ).exists():
            race = Race.objects.create(
                name=players_data[player]["race"]["name"],
                description=players_data[player]["race"]["description"]
            )

        else:
            race = Race.objects.get(
                name=players_data[player]["race"]["name"]
            )

        for skill in players_data[player]["race"]["skills"]:
            if not Skill.objects.filter(
                    name=skill["name"]
            ).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )

        if players_data[player]["guild"]:
            if not Guild.objects.filter(
                    name=players_data[player]["guild"]["name"]
            ).exists():
                guild = Guild.objects.create(
                    name=players_data[player]["guild"]["name"],
                    description=players_data[player]["guild"]["description"]
                )
            else:
                guild = Guild.objects.get(
                    name=players_data[player]["guild"]["name"]
                )
        else:
            guild = None

        Player.objects.create(
            nickname=nickname,
            email=email,
            bio=bio,
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
