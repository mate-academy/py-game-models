import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players_to_create = json.load(file)
    for player_name, player_data in players_to_create.items():
        current_player = Player()
        current_player.nickname = player_name
        current_player.email = player_data.get("email")
        current_player.bio = player_data.get("bio")
        current_player.race = Race.objects.get_or_create(
            name=player_data.get("race").get("name"),
            description=player_data.get("race").get("description"),
        )[0]
        for skill in player_data.get("race").get("skills"):
            Skill.objects.get_or_create(
                name=skill.get("name"),
                bonus=skill.get("bonus"),
                race=current_player.race,
            )
        if player_data.get("guild"):
            current_player.guild = Guild.objects.get_or_create(
                name=player_data.get("guild").get("name"),
                description=player_data.get("guild").get("description"),
            )[0]
        current_player.save()


if __name__ == "__main__":
    main()
