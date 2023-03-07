import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild
import json


def main() -> None:
    with open("players.json") as file:
        data = json.load(file)
        for key in data:
            if not Race.objects.filter(name=data[key]["race"]["name"]).exists():
                race = Race(name=data[key]["race"]["name"],
                            description=data[key]["race"]["description"])
                race.save()
            else:
                race = Race.objects.get(name=data[key]["race"]["name"])

            for skill_name in data[key]["race"]["skills"]:
                if not Skill.objects.filter(name=skill_name["name"]).exists():
                    skill = Skill(name=skill_name["name"],
                                  bonus=skill_name["bonus"], race=race)
                    skill.save()

            if data[key]["guild"] is None:
                guild = None
            else:
                if not Guild.objects.filter(name=data[key]["guild"]["name"]).exists():
                    guild = Guild(name=data[key]["guild"]["name"],
                                  description=data[key]["guild"]["description"])
                    guild.save()
                else:
                    guild = Guild.objects.get(name=data[key]["guild"]["name"])

            if not Player.objects.filter(nickname=key).exists():
                player = Player(nickname=key, email=data[key]["email"],
                                bio=data[key]["bio"], race=race, guild=guild)
                player.save()


if __name__ == "__main__":
    main()
