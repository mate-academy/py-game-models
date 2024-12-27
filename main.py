import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as player_file:
        player_data = json.load(player_file)
    for player_name in player_data.keys():
        info = player_data[player_name]
        email = info["email"]
        bio = info["bio"]
        guild = info["guild"]
        guild_class = Guild.objects.get_or_create(name=guild["name"], description=guild["description"])
        race = info["race"]
        race_class = Race.objects.get_or_create(name=race["name"], description=[race["description"]])
        for skill in race["skills"]:
            Skill.objects.get_or_create(name=skill["name"],
                                        bonus=skill["bonus"],
                                        race=race_class)
        Player.objects.create(nicname=player_name,
                              email=email,
                              bio=bio,
                              race=race_class,
                              guild=guild_class)




if __name__ == "__main__":
    main()
