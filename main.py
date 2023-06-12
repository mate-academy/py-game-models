import datetime

import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)
        for player_name, player_data in data.items():
            player = Player(
                nickname=player_name,
                email=player_data['email'],
                bio=player_data['bio'],
                created_at=datetime.datetime.now()
            )
            player.save()

            race_data = player_data['race']
            race = Race(
                name=race_data['name'],
                description=race_data['description']
            )
            race.save()

            player.race = race

            skills_data = race_data['skills']
            for skill_data in skills_data:
                skill = Skill(
                    name=skill_data['name'],
                    bonus=skill_data['bonus'],
                    race=race
                )
                skill.save()

            guild_data = player_data['guild']
            guild = Guild(
                name=guild_data['name'],
                description=guild_data['description']
            )
            guild.save()

            player.guild = guild

            player.save()


if __name__ == "__main__":
    main()
