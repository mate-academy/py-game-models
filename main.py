import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    def create_guild():


    def create_players():
        with open('players.json', 'r', encoding='utf-8') as file:
            players_data = json.load(file)
        
        for nickname, player_data in players_data.items():
            email = player_data["email"]
            bio = player_data["bio"]
            race_data = player_data["race"]
            guild_data = player_data["guild"]
        
        if guild_data is None:
            guild = None
        else:
            guild = Guild.objects.get_or_create(
                name=player_data["guild"]["name"],
                defaults={
                    "description": player_data["guild"]["description"]
                }
            )[0]

        



if __name__ == "__main__":
    main()
