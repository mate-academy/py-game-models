import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open('players.json', 'r') as file:
        players_data = json.load(file)

    for nickname, player_data in players_data.items():
        # Get or create Race
        race_data = player_data['race']
        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            description=race_data["description"]
        )

        # Get or create Guild
        guild_data = player_data['guild']
        if guild_data is not None:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                description=guild_data["description"]
            )
        else:
            guild = None

        # Create Player
        _ = Player.objects.create(
            nickname=nickname,
            email=player_data['email'],
            bio=player_data['bio'],
            race=race,
            guild=guild
        )

        # Get or create Skills and associate with Race
        skills_data = race_data.get('skills', [])
        for skill_data in skills_data:
            skill, _ = Skill.objects.get_or_create(
                name=skill_data['name'],
                defaults={'bonus': skill_data["bonus"], 'race': race}
            )


if __name__ == "__main__":
    main()
