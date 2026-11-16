import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    def get_or_create_by_name_with_description(
        class_searched: type[Guild] | type [Race],
         attr_name: str
    ) -> Guild | Race:
        class_searched.objects.get_or_create(
                name=player_data[attr_name]["name"],
                defaults={
                    "description": player_data[attr_name]["description"]
                }
            )[0]


    def create_players():
        with open('players.json', 'r', encoding='utf-8') as file:
            players_data = json.load(file)
        
        for nickname, player_data in players_data.items():
            email = player_data["email"]
            bio = player_data["bio"]
            race = get_or_create_by_name_with_description(Race, "race")
            guild = None

            if player_data["guild"] is not None:
                guild = get_or_create_by_name_with_description(Guild, "guild")



if __name__ == "__main__":
    main()
