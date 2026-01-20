import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for nickname, player in players.items():
        race, _ = Race.objects.get_or_create(
            name=player["race"]["name"],
            defaults={"description": player["race"].get("description", "")}
        )

        for skills in player["race"].get("skills", []):
            Skill.objects.get_or_create(
                name=skills["name"],
                defaults={"bonus": skills["bonus"], "race": race}
            )

        guild_data = player.get("guild")
        guild = None
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data.get("name"),
                defaults={"description": guild_data.get("description", "")}
            )

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": player.get("email", ""),
                "bio": player.get("bio", ""),
                "race": race,
                "guild": guild,
            }
        )


if __name__ == "__main__":
    main()
