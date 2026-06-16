import json
from pathlib import Path
from db.models import Player, Race, Guild, Skill


def main() -> None:
    base_dir = Path(__file__).resolve().parent
    players_file = base_dir / "players.json"
    with open(players_file) as f:
        players_data = json.load(f)

    for nickname, player_data in players_data.items():
        race, _ = Race.objects.get_or_create(
            name=player_data["race"]["name"],
            defaults={"description": player_data["race"]["description"]}
        )
        guild_data = player_data.get("guild")
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data.get("description")}
            )
        else:
            guild = None
        for skill in player_data["race"].get("skills", []):
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )
        Player.objects.create(
            nickname=nickname,
            email=player_data["email"],
            bio=player_data.get("bio", ""),
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
