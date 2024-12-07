import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_file:
        players = json.load(players_file)

    for player, data in players.items():

        race, _ = Race.objects.get_or_create(
            name=data["race"]["name"],
            description=data["race"]["description"]
        )

        for skill_data in data["race"].get("skills", []):
            Skill.objects.get_or_create(
                name=skill_data["name"],
                bonus=skill_data["bonus"],
                race=race
            )


        guild = None
        if data.get("guild"):
            guild, _ = Guild.objects.get_or_create(
                name=data["guild"]["name"],
                description=data["guild"]["description"]
            )

        Player.objects.get_or_create(
            nickname=player,
            email=data["email"],
            bio=data["bio"],
            race=race,
            guild=guild
        )



if __name__ == "__main__":
    main()
