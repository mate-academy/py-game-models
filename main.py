import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players:
        players = json.load(players)

    for player_name in players:
        player = players[player_name]
        race, _ = Race.objects.get_or_create(
            name=player["race"]["name"],
            description=player["race"]["description"])

        for skill_data in player["race"]["skills"]:
            skill, _ = Skill.objects.get_or_create(
                name=skill_data["name"],
                bonus=skill_data["bonus"], race=race)

        if player.get("guild"):
            guild, _ = Guild.objects.get_or_create(
                name=player["guild"]["name"],
                description=player["guild"]["description"])
        else:
            guild = None

        Player.objects.get_or_create(
            nickname=player_name,
            email=player["email"],
            bio=player["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
