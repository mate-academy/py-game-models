import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        data = json.load(f)
        for nickname, player_data in data.items():

            # ~~~ Adds race in same table if it is not exist.

            race_data = player_data["race"]
            race, _ = Race.objects.get_or_create(
                name=race_data["name"],
                description=race_data["description"]
            )

            # ~~~ Adds skill in same table if it is not exist.

            if race_data["skills"]:
                for skill in race_data["skills"]:
                    Skill.objects.get_or_create(
                        name=skill["name"],
                        bonus=skill["bonus"],
                        race=race
                    )

            # ~~~ Adds guild in same table if it is not exist.

            guild = None
            if player_data["guild"]:
                guild_data = player_data["guild"]
                guild, _ = Guild.objects.get_or_create(
                    name=guild_data["name"],
                    description=guild_data["description"]
                )

            # ~~~ Adds player in same table if he/she is not exist.

            player, _ = Player.objects.get_or_create(
                nickname=nickname,
                email=player_data["email"],
                bio=player_data["bio"],
                race=race,
                guild=guild
            )

            # Skill.objects.get_or_create(
            #         name="Puff",
            #         bonus="Disintegrate any alive being (even Deathwing)",
            #         race_id=1
            #     )


if __name__ == "__main__":
    # Race.objects.all().delete()
    # Player.objects.all().delete()
    # Guild.objects.all().delete()
    # Skill.objects.all().delete()
    main()
