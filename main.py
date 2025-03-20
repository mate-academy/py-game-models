import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:

    with open("players.json", "r") as file:
        data = json.load(file)

    for player_key, player_info in data.items():
        race, _ = Race.objects.get_or_create(
            name=player_info["race"]["name"],
            description=player_info["race"]["description"]
        )

        skills_data = player_info["race"]["skills"]

        for skill_data in skills_data:
            Skill.objects.get_or_create(
                name=skill_data["name"],
                defaults={"bonus": skill_data["bonus"], "race": race})
        our_guild = data[player_key]["guild"]

        guild_1 = None

        if our_guild:
            guild_1, _ = Guild.objects.get_or_create(
                name=our_guild.get("name", ""),
                description=our_guild.get("description", "")
            )

        nickname = player_key
        email = data[player_key]["email"]
        bio = data[player_key]["bio"]

        race_for_player, _ = Race.objects.get_or_create(
            name=player_info["race"]["name"],
            description=player_info["race"]["description"]
        )

        Player.objects.get_or_create(
            nickname=nickname,
            email=email,
            bio=bio,
            race=race_for_player,
            guild=guild_1
        )


if __name__ == "__main__":
    main()
