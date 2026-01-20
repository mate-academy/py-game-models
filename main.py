import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    # Read data about players from players.json
    with open("players.json", "r") as file:
        players = json.load(file)
        print(players)
    # and add the corresponding entries to the database.
    for name, data in players.items():
        race_data = data["race"]
        guild_data = data["guild"]
        print(race_data)
        print(guild_data)
        print("---")

        # Race
        race_obj, _ =\
            Race.objects.get_or_create(
                name=race_data["name"],
                defaults={"description": race_data.get("description")})
        # Guild
        if guild_data is None:
            print(f"Warning: Player {name} has no guild data.")
            guild_obj = None
        else:
            guild_obj, _ =\
                Guild.objects.get_or_create(
                    name=guild_data["name"],
                    defaults={"description": guild_data.get("description")})

        # Player
        player, created = Player.objects.get_or_create(
            nickname=name,
            bio=data["bio"],
            email=data["email"],
            race=race_obj,
            guild=guild_obj)
        if not created:
            player.bio = data["bio"]
            player.email = data["email"]
            player.race = race_obj
            player.guild = guild_obj
            player.save()

        # Skill on Race
        for skill_data in race_data.get("skills", []):
            skill_obj, created = Skill.objects.get_or_create(
                name=skill_data["name"],
                race=race_obj,
                defaults={"bonus": skill_data.get("bonus", ""),
                          "race": race_obj}
            )


if __name__ == "__main__":
    main()
