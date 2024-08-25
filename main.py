import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file_of_players:
        players = json.load(file_of_players)

    for person in players:
        nickname = person
        email = players[person]["email"]
        bio = players[person]["bio"]

        race_obj, _ = Race.objects.get_or_create(
            name=players[person]["race"]["name"],
            description=players[person]["race"]["description"]
            if players[person]["race"]["description"] else None,
        ) if players[person]["race"] else None

        for skill in players[person]["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race_obj
            )
        if players[person]["guild"]:
            guild_obj, _ = Guild.objects.get_or_create(
                name=players[person]["guild"]["name"],
                description=players[person]["guild"]["description"]
                if players[person]["guild"]["description"] else None,
            )
        else:
            guild_obj = None

        Player.objects.get_or_create(
            nickname=nickname,
            email=email,
            bio=bio,
            race=race_obj,
            guild=guild_obj,
        )


if __name__ == "__main__":
    main()
