import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_file:
        players = json.load(players_file)
    
    for player_id, player_data in players.items():
        player_guild_data = player_data.get("guild")
        if player_guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=player_guild_data["name"],
                defaults={"description": player_guild_data["description"]}
            )
        else:
            guild = None

        race, _ = Race.objects.get_or_create(
            name=player_data["race"]["name"],
            defaults={"description": player_data["race"]["description"]}
        )

        skills_to_add = []
        for skill in player_data["race"].get("skills", []):
            skill_instance, _ = Skill.objects.get_or_create(
                name=skill["name"],
                defaults={"bonus": skill["bonus"], "race": race}
            )
            skills_to_add.append(skill_instance)

        Player.objects.get_or_create(
            nickname=player_id,
            defaults={
                "email": player_data["email"],
                "bio": player_data["bio"],
                "race": race,
                "guild": guild
            }
        )


if __name__ == "__main__":
    main()
    
