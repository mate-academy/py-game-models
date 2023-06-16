import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:

    with open("players.json", "r") as players:
        players_info = json.load(players)

    for player, player_info in players_info.items():
        race_info = player_info["race"]
        race_skills = race_info["skills"]
        guild_info = player_info["guild"]

        race_exists = Race.objects.filter(name=race_info["name"]).exists()
        race = (Race.objects.get(name=race_info["name"])
                if race_exists
                else Race.objects.create(name=race_info["name"],
                                         description=race_info["description"])
                )

        if not race_exists and race_skills:
            for skill in race_skills:
                Skill.objects.create(name=skill["name"],
                                     bonus=skill["bonus"],
                                     race=race)

        guild = None
        if guild_info:
            guild_exists = Guild.objects.filter(name=guild_info["name"]).exists()
            guild = (Guild.objects.get(name=guild_info["name"])
                     if guild_exists
                     else Guild.objects.create(name=guild_info["name"],
                                               description=guild_info["description"]))

        Player.objects.create(nickname=player,
                              email=player_info["email"],
                              bio=player_info["bio"],
                              race=race,
                              guild=guild)


if __name__ == "__main__":
    main()
