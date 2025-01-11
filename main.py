import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for player_data in players:
        race, _ = Race.objects.get_or_create(
            name=players[player_data]["race"]["name"], defaults={
                "description": players[player_data]["race"].get("description", "")
            })

        if players[player_data]["guild"]:
            guild, _ = Guild.objects.get_or_create(
                name=players[player_data]["guild"]["name"], defaults={
                    "description": players[player_data]["guild"].get("description", "")
                })
        else:
            guild = None

        skills = []
        for skill_data in players[player_data]["race"]["skills"]:
            skill, _ = Skill.objects.get_or_create(name=skill_data["name"], defaults={
                "bonus": skill_data["bonus"],
                "race": race
            })
            skills.append(skill)

        Player.objects.get_or_create(
            nickname=player_data, defaults={
                "email": players[player_data]["email"],
                "bio": players[player_data]["bio"],
                "race": race,
                "guild": guild
            }
        )


if __name__ == "__main__":
    main()
