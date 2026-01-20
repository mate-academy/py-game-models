import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data_players = json.load(file)

    for nickname, player_data in data_players.items():

        race_data = player_data["race"]
        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data["description"]}
        )

        for spell in race_data["skills"]:
            skill, _ = Skill.objects.get_or_create(
                name=spell["name"],
                race=race,
                bonus=spell["bonus"]
            )

        guild = None
        guild_data = player_data["guild"]
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data["description"]}
            )

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": player_data["email"],
                "bio": player_data["bio"],
                "race": race,
                "guild": guild,
            }
        )


if __name__ == "__main__":
    main()
