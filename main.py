from sqlite3 import IntegrityError

import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as json_file:
        data = json.load(json_file)

    for player_name, player_data in data.items():
        nickname = player_name
        email = player_data["email"]
        bio = player_data["bio"]
        race_data = player_data["race"]
        guild_data = player_data["guild"]
        skills_data = race_data.get("skills", [])

        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            description=race_data["description"])

        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                description=guild_data.get("description", ""))
        else:
            guild = None

        player = Player(
            nickname=nickname,
            email=email,
            bio=bio,
            race=race,
            guild=guild
        )

        try:
            player.save()
        except IntegrityError:

            existing_player = Player.objects.get(nickname=nickname)
            existing_player.email = email
            existing_player.bio = bio
            existing_player.race = race
            existing_player.guild = guild
            existing_player.save()

        for skill_data in skills_data:
            skill, _ = Skill.objects.get_or_create(
                name=skill_data["name"],
                bonus=skill_data["bonus"],
                race=race
            )


if __name__ == "__main__":
    main()
