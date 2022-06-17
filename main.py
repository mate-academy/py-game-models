import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main():
    with open("players.json") as players_data:
        players = json.load(players_data)

    for player_nick, player_info in players.items():
        race_info = player_info["race"]
        race, _ = Race.objects.get_or_create(
            name=race_info["name"],
            description=race_info["description"])

        for skill in race_info["skills"]:
            Skill.objects.get_or_create(**skill, race=race)

        guild_info = player_info["guild"]
        guild, _ = Guild.objects.get_or_create(**guild_info)\
            if guild_info else (None, _)

        Player.objects.create(
            nickname=player_nick, email=player_info["email"],
            bio=player_info["bio"], race=race, guild=guild)


if __name__ == "__main__":
    main()
