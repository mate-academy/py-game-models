import json
from db.models import Race, Skill, Player, Guild
from django.db import transaction


def main() -> None:
    with open("players.json") as f:
        players_data = json.load(f)

    with transaction.atomic():
        for nickname, player_data in players_data.items():
            race, _ = Race.objects.get_or_create(
                name=player_data["race"]["name"],
                description=player_data["race"]["description"]
            )

            guild = None
            if player_data["guild"]:
                guild, _ = Guild.objects.get_or_create(
                    name=player_data["guild"]["name"],
                    description=player_data["guild"]["description"]
                )

            Player.objects.create(
                nickname=nickname,
                email=player_data["email"],
                bio=player_data["bio"],
                race=race,
                guild=guild
            )

            for skill_data in player_data["race"]["skills"]:
                skill, _ = Skill.objects.get_or_create(
                    name=skill_data["name"],
                    bonus=skill_data["bonus"],
                    race=race
                )


if __name__ == "__main__":
    main()
