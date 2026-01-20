import json
from db.models import Race, Skill, Guild, Player
from django.db import transaction


def main() -> None:
    players_data = load_data()
    add_players_to_database(players_data)


def load_data() -> dict:
    with open("players.json", "r") as f:
        players_data = json.load(f)
        return players_data


@transaction.atomic
def add_players_to_database(players_data: dict) -> None:
    for player_name, player_data in players_data.items():
        email = player_data["email"]
        bio = player_data["bio"]
        race_data = player_data["race"]
        guild_data = player_data.get("guild")

        race, race_created = Race.objects.get_or_create(
            name=race_data["name"],
            description=race_data.get("description", "")
        )

        if guild_data:
            guild, guild_created = Guild.objects.get_or_create(
                name=guild_data["name"],
                description=guild_data.get("description", "")
            )
        else:
            guild = None

        player, created = Player.objects.get_or_create(
            nickname=player_name,
            email=email,
            bio=bio,
            race=race,
            guild=guild
        )

        if race_created:
            for skill_data in race_data["skills"]:
                Skill.objects.create(
                    name=skill_data["name"],
                    bonus=skill_data["bonus"],
                    race=race
                )


if __name__ == "__main__":
    main()
