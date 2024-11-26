import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    # Load data from players.json
    with open('players.json') as f:
        players_data = json.load(f)

    for player_data in players_data:
        # Get or create the race
        race, created = Race.objects.get_or_create(name=player_data['race'])

        # Get or create the guild
        guild, created = Guild.objects.get_or_create(name=player_data['guild'])

        # Create skills for the race
        for skill_data in player_data['skills']:
            # Ensure each skill is associated with the race
            Skill.objects.get_or_create(
                name=skill_data['name'],
                bonus=skill_data['bonus'],
                race=race
            )

        # Create the player
        Player.objects.get_or_create(
            nickname=player_data['nickname'],
            email=player_data['email'],
            bio=player_data['bio'],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
