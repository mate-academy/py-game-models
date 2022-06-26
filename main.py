import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild

PLAYERS = "players.json"


def load_data_json():
    with open(PLAYERS) as file:
        return json.load(file)


def get_race_info():
    return [value["race"] for key, value in load_data_json().items()]


def create_race_and_skill_model():
    """
    This function making Skill and Race models
    """
    data = get_race_info()
    for race in data:
        if not Race.objects.filter(name=race["name"]).exists():
            Race.objects.create(name=f"{race['name']}",
                                description=f"{race['description']}")

        for skill in race["skills"]:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(name=skill['name'],
                                     bonus=skill['bonus'],
                                     race=Race.objects.get(
                                         name=f"{race['name']}"))


def create_guild_model():
    """
    This function making Guild models
    """
    data = load_data_json()
    guilds_data = [value["guild"] for key, value in data.items()]
    for guild in guilds_data:
        if guild is not None:
            if not Guild.objects.filter(name=guild["name"]).exists():
                if guild["description"] is not None:
                    Guild.objects.create(name=guild["name"],
                                         description=guild["description"])

                else:
                    Guild.objects.create(name=guild["name"],
                                         description=None)


def create_player_model():
    data = load_data_json()
    for key, value in data.items():
        if not Player.objects.filter(nickname=key).exists():
            if value["guild"] is not None:
                Player.objects.create(nickname=key,
                                      email=value["email"],
                                      bio=value["bio"],
                                      race=Race.objects.get(
                                          name=value["race"]["name"]),
                                      guild=Guild.objects.get(
                                          name=value["guild"]["name"]))
            else:
                Player.objects.create(nickname=key,
                                      email=value["email"],
                                      bio=value["bio"],
                                      race=Race.objects.get(
                                          name=value["race"]["name"]),
                                      guild=None)


def main():
    create_race_and_skill_model()
    create_guild_model()
    create_player_model()


if __name__ == "__main__":
    main()
