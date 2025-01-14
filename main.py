import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)
        for nickname, i in data.items():
            race, _ = Race.objects.get_or_create(name= i["race"]["name"], description=i["race"]["description"])
            for skill in i["race"]["skills"]:
                Skill.objects.get_or_create(name=skill["name"], bonus=skill["bonus"], race=race)
            guild = None
            if i["guild"] is not None:
                guild, _ = Guild.objects.get_or_create(name=i["guild"]["name"], description=i["guild"]["description"])
            Player.objects.get_or_create(nickname=nickname, email=i["email"], bio=i["bio"], race=race, guild=guild)



if __name__ == "__main__":
    main()
