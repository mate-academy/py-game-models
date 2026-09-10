import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for nickname, values in players.items():
        player_email = values["email"]
        player_bio = values["bio"]
        player_race = values["race"]
        race, _ = Race.objects.get_or_create(
            name=player_race["name"],
            defaults={"description": player_race["description"]}
        )
        for data in player_race["skills"]:
            skill, _ = Skill.objects.get_or_create(
                name=data["name"],
                defaults={"bonus": data["bonus"], "race": race}
            )
        guild_data = values.get("guild")
        guild = None
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data["description"]}
            )
        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": player_email,
                "bio": player_bio,
                "race": race,
                "guild": guild
            }
        )


if __name__ == "__main__":
    main()
