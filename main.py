import json
import os


from db.models import Race, Skill, Player, Guild


def main() -> None:
    json_path = os.path.join(os.path.dirname(__file__), "players.json")

    with open(json_path, "r", encoding="utf-8") as f:
        players_data = json.load(f)  # top-level dict keyed by player nickname

    # Iterate over each player object
    for nickname, player_data in players_data.items():
        # ---- Race ----
        race_data = player_data.get("race", {})
        race_name = race_data.get("name")
        race_description = race_data.get("description", "")
        if race_name:
            race, _ = Race.objects.get_or_create(
                name=race_name,
                defaults={"description": race_description},
            )
        else:
            race = None  # handle missing race safely

        # ---- Skills ----
        for skill_data in race_data.get("skills", []):
            skill_name = skill_data.get("name")
            skill_bonus = skill_data.get("bonus", "")
            if skill_name and race:
                Skill.objects.get_or_create(
                    name=skill_name,
                    defaults={"bonus": skill_bonus, "race": race},
                )
        # No reassignment of skill.race — safe for unique constraint

        # ---- Guild ----
        guild_data = player_data.get("guild")
        guild = None
        if guild_data:
            guild_name = guild_data.get("name")
            guild_description = guild_data.get("description")
            if guild_name:
                guild, _ = Guild.objects.get_or_create(
                    name=guild_name,
                    defaults={"description": guild_description},
                )

        # ---- Player ----
        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": player_data.get("email", ""),
                "bio": player_data.get("bio", ""),
                "race": race,
                "guild": guild,
                # created_at handled by model default
            },
        )


if __name__ == "__main__":
    main()
