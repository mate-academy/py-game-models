import json
import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as p:
        players = json.load(p)

    for player_name, player_data in players.items():
        player_bio = player_data["bio"]
        player_email = player_data["email"]
        player_race_data = player_data["race"]

        player_race, created = Race.objects.get_or_create(
            name=player_race_data["name"],
            description=player_race_data["description"]
        )

        for player_race_skill in player_data["race"]["skills"]:
            skill, created = Skill.objects.get_or_create(
                name=player_race_skill["name"],
                bonus=player_race_skill["bonus"],
                race=player_race
            )

        player_guild_data = player_data["guild"]
        player_guild = None
        if player_guild_data:
            player_guild, created = Guild.objects.get_or_create(
                name=player_guild_data["name"],
                description=player_guild_data["description"]
            )

        Player.objects.get_or_create(
            nickname=player_name,
            bio=player_bio,
            email=player_email,
            race=player_race,
            guild=player_guild
        )


if __name__ == "__main__":
    main()
