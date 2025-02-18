import json
from db.models import Race, Skill, Guild, Player


def main() -> None:
    with open("players.json", "r") as file:
        players_data = json.load(file)

    for nickname, player_data in players_data.items():
        race_data = player_data.get("race", {})
        guild_data = player_data.get("guild", {})

        race, _ = Race.objects.get_or_create(
            name=race_data.get("name"),
            defaults={"description": race_data.get("description", "")},
        )

        for skill_data in race_data.get("skills", []):
            Skill.objects.get_or_create(
                name=skill_data.get("name"),
                defaults={"bonus": skill_data.get("bonus"), "race": race},
            )

        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data.get("name"),
                defaults={"description": guild_data.get("description", "")},
            )
        else:
            guild = None

        Player.objects.create(
            nickname=nickname,
            email=player_data.get("email"),
            bio=player_data.get("bio"),
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
