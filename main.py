import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)
        print(players)
    for player in players.values():
        race, created = Race.objects.get_or_create(name=player["race"]["name"],
                                                   description=player["race"]["description"])
        guild = None
        if player.get("guild"):
            guild, created = Guild.objects.get(name=player["guild"]["name"],
                                               description=player["guild"]["description"])

        play = Player.objects.create(nickname=player["nickname"], email=player["email"],
                                     bio=player["bio"], race=race, guild=guild)
        for skill in player["race"]["skills"]:
            Skill.objects.get_or_create(name=skill["name"], bonus=skill["bonus"],)


if __name__ == "__main__":
    main()
