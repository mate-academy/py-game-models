import init_django_orm # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)
    for player_name, player in players.items():
        try:
            race = Race.objects.get(name=player.get("race").get("name"))
        except Exception:
            race = Race.objects.create(name=player.get("race").get("name"),
                                       description=player.get("race").get("description"))
        try:
            guild = Guild.objects.get(name=player["guild"]["name"])
        except TypeError:
            guild = None
        except Exception:
            guild = Guild.objects.create(name=player["guild"]["name"],
                                         description=player["guild"]["description"])
        for skill_data in player.get("race").get("skills"):
            try:
                skill = Skill.objects.get(name=skill_data.get("name"))
            except Exception:
                skill = Skill.objects.create(name=skill_data.get("name"),bonus=skill_data.get("bonus"), race=race)
        Player.objects.create(nickname=player_name,
                              email=player["email"],
                              bio=player["bio"],
                              race=race,
                              guild=guild)

if __name__ == "__main__":
    main()
