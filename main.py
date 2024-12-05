import json
from db.models import Race, Skill, Guild, Player
from django.db.utils import IntegrityError


def main() -> None:
    with open("players.json", "r") as file:
        players_data = json.load(file)

    for player_name, player_data in players_data.items():
        race, created = Race.objects.get_or_create(
            name=player_data["race"]["name"],
            defaults={"description": player_data["race"]["description"]}
        )

        guild_data = player_data.get("guild", {})
        guild = None
        if guild_data is not None:
            guild, created = (Guild.objects.get_or_create(
                name=guild_data.get("name", ""),
                defaults={"description": guild_data.get("description")})
            )

        try:
            player, created = Player.objects.get_or_create(
                nickname=player_name,
                email=player_data["email"],
                bio=player_data["bio"],
                race=race,
                guild=guild
            )
        except IntegrityError:
            print(f"Player with nickname or email '{player_name}"
                  f"'/'{player_data['email']}' already exists.")

        for skill_data in player_data["race"]["skills"]:
            skill, created = Skill.objects.get_or_create(
                name=skill_data["name"],
                bonus=skill_data["bonus"],
                race=race
            )


if __name__ == "__main__":
    main()
