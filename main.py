import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data_players = json.load(file)

    for nickname, guild_data in data_players.items():
        p_email = guild_data["email"]
        p_bio = guild_data["bio"]
        race, _ = Race.objects.get_or_create(
            name=guild_data["race"]["name"],
            defaults={"description": guild_data["race"]["description"]}
        )
        for sk_player in guild_data["race"]["skills"]:
            Skill.objects.get_or_create(
                name=sk_player["name"],
                defaults={
                    "bonus": sk_player["bonus"],
                    "race": race
                }
            )
        guild = None
        guild_data = guild_data.get("guild")
        if guild_data is not None:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data["description"]}
            )

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": p_email,
                "bio": p_bio,
                "race": race,
                "guild": guild
            }
        )


if __name__ == "__main__":
    main()
