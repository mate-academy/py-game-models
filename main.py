import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as config_file:
        players_data = json.load(config_file)

    for player, data in players_data.items():

        race = Race.objects.get_or_create(name=data["race"]["name"],
                                          defaults={"name": data["race"]["name"], # noqa
                                           "description": data["race"]["description"]})[0] # noqa
        if data["guild"]:
            guild = Guild.objects.get_or_create(name=data["guild"]["name"],
                                                defaults={"name": data["guild"]["name"], # noqa
                                                "description": data["guild"]["description"]})[0] # noqa
        else:
            guild = None

        for skill in data["race"]["skills"]:
            Skill.objects.get_or_create(name=skill["name"],
                                        defaults={"name": skill["name"],
                                                  "bonus": skill["bonus"],
                                                  "race": race})
        Player.objects.create(nickname=player,
                              email=data["email"],
                              bio=data["bio"],
                              race=race,
                              guild=guild)


if __name__ == "__main__":
    main()
