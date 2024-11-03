import json
from db.models import Race, Skill, Player, Guild


def read_file() -> object:
    with open("players.json", "r") as players_file:
        players = json.load(players_file)
    return players


def main() -> None:
    players_data = read_file()

    for player_name, player_data in players_data.items():
        guild_data = player_data.get("guild")
        guild = None
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data.get("description")}
            )

        race_data = player_data["race"]
        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data.get("description")}
        )

        skills = []
        for skill_data in race_data.get("skills", []):
            skill, _ = Skill.objects.get_or_create(
                name=skill_data["name"],
                defaults={"bonus": skill_data["bonus"], "race": race}
            )
            skills.append(skill)

        player, created = Player.objects.get_or_create(
            nickname=player_name,
            defaults={
                "email": player_data["email"],
                "bio": player_data["bio"],
                "race": race,
                "guild": guild
            }
        )


if __name__ == "__main__":
    main()
