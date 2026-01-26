import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players_to_create = json.load(file)
    for player_name, player_data in players_to_create.items():
        current_player = Player()
        current_player.nickname = player_name
        current_player.email = player_data["email"]
        current_player.bio = player_data["bio"]
        current_player.race = Race.objects.get_or_create(
            name=player_data["race"]["name"],
            description=player_data["race"]["description"]
        )
        for skill in player_data["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=current_player.race
            )
        current_player.guild = Guild.objects.get_or_create(
            name=player_data["guild"]["name"],
            description=player_data["guild"]["description"]
        )
        current_player.save()


if __name__ == "__main__":
    main()
