import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players_data = json.load(file)
        for nickname, player_info in players_data.items():

            # create race
            race_name = player_info["race"]["name"]
            race_description = player_info["race"]["description"]
            race, _ = Race.objects.get_or_create(
                name=race_name,
                description=race_description
            )
            # race_id = Race.objects.get(name=race_name).id

            # create skills
            for skill in player_info["race"]["skills"]:
                skill_name = skill["name"]
                skill_bonus = skill["bonus"]
                Skill.objects.get_or_create(
                    name=skill_name,
                    bonus=skill_bonus,
                    race=race
                )

            # create guild
            if player_info.get("guild"):
                guild_name = player_info["guild"]["name"]
                guild_description = player_info["guild"]["description"]
                guild, _ = Guild.objects.get_or_create(
                    name=guild_name,
                    description=guild_description
                )
            else:
                guild = None

            # create player
            email = player_info["email"]
            bio = player_info["bio"]
            Player.objects.get_or_create(
                nickname=nickname,
                email=email, bio=bio,
                race=race,
                guild=guild
            )


if __name__ == "__main__":
    main()
