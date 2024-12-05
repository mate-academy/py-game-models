import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players_data = json.load(file)
    for player_name, player_data in players_data.items():
        new_race, _ = Race.objects.get_or_create(
            name=player_data["race"].get("name"),
            description=player_data["race"].get("description"),
        )
        if player_data["guild"]:
            new_guild, _ = Guild.objects.get_or_create(
                name=player_data["guild"].get("name"),
                description=player_data["guild"].get("description"),
            )
        else:
            new_guild = None
        for skill in player_data["race"]["skills"]:
            if not Skill.objects.filter(name=skill.get("name")).exists():
                Skill.objects.create(
                    name=skill.get("name"),
                    bonus=skill.get("bonus"),
                    race=new_race
                )
        Player.objects.create(
            nickname=player_name,
            email=player_data.get("email"),
            bio=player_data.get("bio"),
            race=new_race,
            guild=new_guild,
        )


if __name__ == "__main__":
    main()
