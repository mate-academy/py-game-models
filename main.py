import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    Race.objects.all().delete()
    Skill.objects.all().delete()
    Guild.objects.all().delete()
    Player.objects.all().delete()

    with open("players.json", "r") as f:
        players_data = json.load(f)

        for nickname, player_data in players_data.items():
            race_name = player_data.get("race", {}).get("name", "")
            race_description = player_data.get(
                "race", {}
            ).get("description", "")

            skills_list = player_data.get("race", {}).get("skills", [])

            email_ = player_data.get("email")
            bio = player_data.get("bio")

            if any(race[0] == race_name for race in Race.RACES):
                Race.objects.get_or_create(
                    name=race_name,
                    defaults={
                        "name": race_name,
                        "description": race_description
                    }
                )

            player_race = Race.objects.get(name=race_name)

            if skills_list:
                for skill in skills_list:
                    Skill.objects.get_or_create(
                        name=skill["name"],
                        defaults={
                            "name": skill["name"],
                            "bonus": skill["bonus"],
                            "race": player_race
                        }
                    )

            if "guild" in player_data and player_data["guild"]:
                guild_name = player_data["guild"].get("name")
                guild_description = player_data["guild"].get("description")

                Guild.objects.get_or_create(
                    name=guild_name,
                    defaults={"description": guild_description}
                )
                try:
                    player_guild = Guild.objects.get(name=guild_name)
                except Guild.DoesNotExist:
                    print(f"Guild '{guild_name}' does not exist.")
            else:
                player_guild = None

            try:
                Player.objects.get_or_create(
                    nickname=nickname,
                    defaults={
                        "email": email_,
                        "bio": bio,
                        "race": player_race,
                        "guild": player_guild,
                    }
                )
            except Race.DoesNotExist:
                print(f"Race '{race_name}' does not exist in the database.")
                continue


if __name__ == "__main__":
    main()
