import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as f:
        players_info = json.load(f)

    for player_name, player_attributes in players_info.items():
        race, is_race_created = Race.objects.get_or_create(
            name=player_attributes["race"]["name"],
            description=player_attributes["race"]["description"]
        )

        for skill in player_attributes["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )

        guild = player_attributes.get("guild")
        if guild:
            guild, is_guild_created = Guild.objects.get_or_create(
                name=guild["name"],
                description=guild["description"]
            )

        Player.objects.get_or_create(
            nickname=player_name,
            email=player_attributes["email"],
            bio=player_attributes["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
