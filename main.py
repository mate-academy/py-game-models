import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    Race.objects.all().delete()
    Skill.objects.all().delete()
    Player.objects.all().delete()
    Guild.objects.all().delete()

    with open('players.json', 'r') as players_file:
        players_json = json.load(players_file)

    for player_name, player_data in players_json.items():
        email = player_data['email']
        bio = player_data['bio']
        race_data = player_data['race']
        guild_data = player_data.get('guild')
        skills_data = race_data.get('skills', [])

        # Making Race or passing
        race, created = Race.objects.get_or_create(
            name=race_data['name'],
            defaults={"description": race_data.get("description", "")}
        )

        # Making a Guild or passing
        if guild_data:
            guild, created = Guild.objects.get_or_create(
                name=guild_data['name'],
                defaults={"description": guild_data.get('description', "")}
            )
        else:
            guild = None

        # Making a Skill or passing
        for skill_data in skills_data:
            skill, created = Skill.objects.get_or_create(
                name=skill_data['name'],
                defaults={"bonus": skill_data["bonus"], "race": race}
            )

        # Making a Player
        Player.objects.create(
            nickname=player_name,
            email=email,
            bio=bio,
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
