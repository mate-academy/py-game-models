import json
from django.utils.datetime_safe import datetime
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players_data = json.load(file)

    for nickname, player_data in players_data.items():
        race, _ = Race.objects.get_or_create(
            name=player_data["race"]["name"],
            defaults={"description": player_data["race"]["description"]}
        )

        guild = None
        if player_data.get("guild"):
            guild, _ = Guild.objects.get_or_create(
                name=player_data["guild"]["name"],
                defaults={"description": player_data["guild"]["description"]}
            )

        Player.objects.create(
            nickname=nickname,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race,
            guild=guild,
            created_at=datetime.now(),
        )

        for skill_data in player_data["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill_data["name"],
                race=race,
                defaults={"bonus": skill_data["bonus"]}
            )


if __name__ == "__main__":
    main()
