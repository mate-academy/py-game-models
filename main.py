import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players_data = json.load(file)

    for player_name, player_data in players_data.items():
        guild_data = player_data.get("guild")
        guild_name = guild_data["name"] if guild_data else None

        race_name = player_data["race"]["name"]

        if guild_name is not None:
            guild, _ = Guild.objects.get_or_create(
                name=guild_name,
                description=guild_data["description"] if guild_data else None,
            )
        else:
            guild = None

        race, _ = Race.objects.get_or_create(
            name=race_name, description=player_data["race"]["description"]
        )

        for skill_data in player_data["race"]["skills"]:
            skill_name = skill_data["name"]
            skill_bonus = skill_data["bonus"]

            skill, _ = Skill.objects.get_or_create(
                name=skill_name, bonus=skill_bonus, race=race
            )

        player, _ = Player.objects.get_or_create(
            nickname=player_name,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
