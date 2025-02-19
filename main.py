import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as players_file:
        players = json.load(players_file)

    for nickname, player_data in players.items():
        race, _ = Race.objects.get_or_create(
            name=player_data["race"]["name"],
            defaults={"description": player_data["race"]["description"]}
        )

        for skills in player_data["race"]["skills"]:
            if player_data["race"]["skills"]:
                Skill.objects.get_or_create(
                    name=skills["name"],
                    defaults={
                        "bonus": skills["bonus"],
                        "race": race
                }
            )

        guild = None
        if player_data["guild"]:
            guild, _ = Guild.objects.get_or_create(
                name=player_data["guild"]["name"],
                defaults={"description": player_data["guild"]["description"]}
            )

        Player.objects.get_or_create(
            nickname=nickname,
            race=race,
            guild=guild,
            defaults={
                "email": player_data["email"],
                "bio": player_data["bio"]
            }
        )




if __name__ == "__main__":
    main()
