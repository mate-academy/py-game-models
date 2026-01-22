import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players = json.load(file)
    for data_player in players:
        user = players[data_player]
        skills = user.get("race").get("skills")
        guild = None
        if user.get("guild"):
            guild, _ = Guild.objects.get_or_create(
                name=user.get("guild").get("name"),
                description=user.get("guild").get("description"))
        race, _ = Race.objects.get_or_create(
            name=user.get("race").get("name"),
            description=user.get("race").get("description"))

        player, _ = Player.objects.get_or_create(
            nickname=data_player,
            email=user.get("email"),
            bio=user.get("bio"),
            race=race,
            guild=guild
        )
        for skill in skills:
            Skill.objects.get_or_create(
                name=skill.get("name"),
                bonus=skill.get("bonus"),
                race=player.race)


if __name__ == "__main__":
    main()
