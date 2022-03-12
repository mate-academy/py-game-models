import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main():
    with open("players.json") as file_read:
        players = json.load(file_read)
        for player in players:
            player_data = players[player]
            player_race_data = player_data["race"]
            player_race_name = player_race_data["name"]
            if not Race.objects.filter(name=player_race_name).exists():
                player_race_description = player_race_data["description"]
                Race.objects.create(
                    name=player_race_name,
                    description=player_race_description
                )
            player_race = Race.objects.get(name=player_race_name)
            for skill in player_race_data["skills"]:
                skill_name = skill["name"]
                if not Skill.objects.filter(name=skill_name).exists():
                    skill_bonus = skill["bonus"]
                    Skill.objects.create(
                        name=skill_name,
                        bonus=skill_bonus,
                        race=player_race
                    )
            player_guild_data = player_data["guild"]
            if player_guild_data:
                player_guild_name = player_guild_data["name"]
                if not Guild.objects.filter(name=player_guild_name).exists():
                    player_guild_description = player_guild_data["description"]
                    Guild.objects.create(
                        name=player_guild_name,
                        description=player_guild_description
                    )
                player_guild = Guild.objects.get(name=player_guild_name)
            else:
                player_guild = None
            if not Player.objects.filter(nickname=player).exists():
                Player.objects.create(
                    nickname=player,
                    email=player_data["email"],
                    bio=player_data["bio"],
                    race=player_race,
                    guild=player_guild
                )


if __name__ == "__main__":
    main()
