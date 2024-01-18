import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        data = json.load(f)
        for nickname, player_data in data.items():

            # ~~~ Adds race in same table if it is not exist.

            race, race_description, skills = player_data["race"].values()
            print(race, race_description)
            players_race = Race.objects.get_or_create(name=race, description=race_description)

            # ~~~ Adds skill in same table if it is not exist.

            if skills:
                for skill in skills:
                    Skill.objects.get_or_create(
                        name=skill["name"],
                        bonus=skill["bonus"],
                        race_id=Race.objects.get(name=race).id
                    )

            # ~~~ Adds guild in same table if it is not exist.

            guild_id = None
            if player_data["guild"]:
                guild, guild_description = player_data["guild"].values()
                players_guild = Guild.objects.get_or_create(
                    name=guild,
                    description=guild_description
                )
                guild_id = Guild.objects.get(name=guild).id

            # ~~~ Adds player in same table if he/she is not exist.

            current_player = Player.objects.get_or_create(
                nickname=nickname,
                email=player_data["email"],
                bio=player_data["bio"],
                race_id=Race.objects.get(name=race).id,
                guild_id=guild_id
            )

            # Skill.objects.get_or_create(
            #         name="Puff",
            #         bonus="Disintegrate any alive being (even Deathwing)",
            #         race_id=1
            #     )


if __name__ == "__main__":
    main()
