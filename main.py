import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open('players.json', 'r') as f:
        players_data = json.load(f)

    for player_name, player_data in players_data.items():
        race, _ = Race.objects.get_or_create(
            name=player_data["race"]["name"],
            description=player_data["race"]["description"]
            )
        if player_data["guild"]:
            guild, _ = Guild.objects.get_or_create(
                name=player_data["guild"]["name"],
                description=player_data["guild"]["description"]
            )
        else:
            guild = None

        skills = []
        for skill_data in player_data["race"]["skills"]:
            skill, _ = Skill.objects.get_or_create(
                name=skill_data["name"],
                bonus=skill_data["bonus"],
                race=race
            )
            skills.append(skill)

        player = Player.objects.create(
            nickname=player_name,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race,
            guild=guild

        )
        player.skills.set(skills)


if __name__ == "__main__":
    main()
