import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild
import json


def main() -> None:
    with open("players.json", "r") as file:
        players_data = json.load(file)
    for nickname, player_data in players_data.items():
        race, created = Race.objects.get_or_create(
            name=player_data["race"]["name"],
            defaults={"description": player_data["race"]["description"]}
        )
        guild = None
        if player_data["guild"] is not None:
            guild, created = Guild.objects.get_or_create(
                name=player_data["guild"]["name"],
                defaults={"description": player_data["guild"]["description"]},
            )
        for skill in player_data["race"]["skills"]:
            skills, created = Skill.objects.get_or_create(
                name=skill["name"],
                defaults={"bonus": skill["bonus"]},
                race=race
            )
        Player.objects.create(
            nickname=nickname,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
