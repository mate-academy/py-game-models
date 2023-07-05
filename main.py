import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild
import json


def main() -> None:
    with open("players.json") as players_data_file:
        people = json.load(players_data_file)
    for person in people:
        race, created = Race.objects.get_or_create(
            name=people[person]["race"]["name"],
            description=people[person]["race"]["description"]
        )

        for skill_name in people[person]["race"]["skills"]:
            if not Skill.objects.filter(name=skill_name["name"]).exists():
                Skill.objects.create(name=skill_name["name"],
                                     bonus=skill_name["bonus"], race=race)
        if people[person]["guild"] is None:
            guild = None
        else:
            guild, created = Guild.objects.get_or_create(
                name=people[person]["guild"]["name"],
                description=people[person]["guild"]["description"]
            )

        if not Player.objects.filter(nickname=person).exists():
            Player.objects.create(nickname=person,
                                  email=people[person]["email"],
                                  bio=people[person]["bio"],
                                  race=race,
                                  guild=guild)


if __name__ == "__main__":
    main()
