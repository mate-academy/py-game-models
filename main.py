import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players_data = json.load(file)
        for nickname, value in players_data.items():

            # create race
            for _ in value["race"]:
                race_name = value["race"]["name"]
                race_description = value["race"]["description"]
                if not Race.objects.filter(name=race_name).exists():
                    Race.objects.create(
                        name=race_name,
                        description=race_description
                    )
                race_id = Race.objects.get(name=race_name).id

                # create skills
                for skill in value["race"]["skills"]:
                    skill_name = skill["name"]
                    skill_bonus = skill["bonus"]
                    if not Skill.objects.filter(name=skill_name).exists():
                        Skill.objects.create(
                            name=skill_name,
                            bonus=skill_bonus,
                            race_id=race_id
                        )

            # create guild
            if value["guild"]:
                guild_name = value["guild"]["name"]
                guild_description = value["guild"]["description"]
                if not Guild.objects.filter(name=guild_name).exists():
                    Guild.objects.create(
                        name=guild_name,
                        description=guild_description
                    )
                guild_id = Guild.objects.get(name=guild_name).id
            else:
                guild_id = None
            email = value["email"]
            bio = value["bio"]

            # create player
            if not Player.objects.filter(nickname=nickname).exists():
                Player.objects.create(
                    nickname=nickname,
                    email=email, bio=bio,
                    race_id=race_id,
                    guild_id=guild_id
                )


if __name__ == "__main__":
    main()
