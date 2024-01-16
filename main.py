import init_django_orm  # noqa: F401
import json
import datetime

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as f:
        players = json.load(f)

    for player_name, player_data in players.items():
        rasa, _ = Race.objects.get_or_create(
            name=player_data["race"]["name"],
            description=player_data["race"]["description"]
        )

        for skill_data in player_data["race"]["skills"]:
            skill, _1 = Skill.objects.get_or_create(
                name=skill_data["name"],
                bonus=skill_data["bonus"],
                race=rasa
            )
        guild = None
        if player_data["guild"] is not None:
            guild, _2 = Guild.objects.get_or_create(
                name=player_data["guild"]["name"],
                description=player_data["guild"]["description"]
            )

        Player.objects.create(
            nickname=player_name,
            email=player_data["email"],
            bio=player_data["bio"],
            race=rasa,
            guild=guild,
            created_at=datetime.time()
        )


if __name__ == "__main__":
    main()
