import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        data = json.load(f)
        for nickname, player_data in data.items():

            # ~~~ Adds race in same table if it is not exist.

            players_race = Race.objects.get_or_create(
                name=player_data["race"]["name"],
                description=player_data["race"]["description"]
            )

            # ~~~ Adds skill in same table if it is not exist.

            if player_data["race"]["skills"]:
                for skill in player_data["race"]["skills"]:

                    Skill.objects.get_or_create(
                        name=skill["name"],
                        bonus=skill["bonus"],
                        race_id=Race.objects.get(name=player_data["race"]["name"]).id
                    )

            # ~~~ Adds guild in same table if it is not exist.

            guild_id = None
            if player_data["guild"]:
                players_guild = Guild.objects.get_or_create(
                    name=player_data["guild"]["name"],
                    description=player_data["guild"]["description"]
                )
                guild_id = Guild.objects.get(name=player_data.get("guild")["name"]).id

            # ~~~ Adds player in same table if he/she is not exist.

            current_player = Player.objects.get_or_create(
                nickname=nickname,
                email=player_data["email"],
                bio=player_data["bio"],
                race_id=Race.objects.get(name=player_data["race"]["name"]).id,
                guild_id=guild_id
            )

            # Skill.objects.get_or_create(
            #         name="Puff",
            #         bonus="Disintegrate any alive being (even Deathwing)",
            #         race_id=1
            #     )


if __name__ == "__main__":
    main()
