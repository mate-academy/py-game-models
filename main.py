import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as player_file:
        player_data = json.load(player_file)
    for player_name in player_data.keys():
        info = player_data[player_name]
        email = info.get("email")
        bio = info.get("bio")
        guild = info.get("guild")
        if guild is not None:
            guild_class, _ = Guild.objects.get_or_create(
                name=guild["name"],
                description=guild["description"])
        race = info.get("race")
        race_class, _ = Race.objects.get_or_create(
            name=race["name"],
            description=[race["description"]])
        for skill in race["skills"]:
            skill_class, _ = Skill.objects.get_or_create(name=skill["name"],
                                                         bonus=skill["bonus"],
                                                         race=race_class)
        Player.objects.create(nickname=player_name,
                              email=email,
                              bio=bio,
                              race=race_class,
                              guild=guild_class)


if __name__ == "__main__":
    main()
