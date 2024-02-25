# main.py
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)
        for player_data in data:
            race, _ = Race.objects.get_or_create(
                name=player_data["race"]["name"],
                defaults={"description": player_data["race"]["description"]}
            )
            guild, _ = Guild.objects.get_or_create(
                name=player_data["guild"]["name"],
                defaults={"description": player_data["guild"]["description"]}
            )
            player, _ = Player.objects.get_or_create(
                nickname=player_data["nickname"],
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
