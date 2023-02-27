import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "rb") as file:
        players_data = json.load(file)

        for key_name in players_data:

            if Race.objects.filter(
                    name=players_data[key_name].get("race").get("name")
            ).exists():
                race = Race.objects.filter(
                    name=players_data[key_name].get("race").get("name")
                )[0]

            else:
                race = Race(
                    name=players_data[key_name].get("race").get("name"),
                    description=players_data[key_name].get(
                        "race"
                    ).get("description")
                )

            race.save()

            for skill in players_data[key_name].get("race").get("skills"):
                if Skill.objects.filter(name=skill.get("name")):
                    skill_model = Skill.objects.filter(
                        name=skill.get("name")
                    )[0]

                else:
                    skill_model = Skill(
                        name=skill.get("name"),
                        bonus=skill.get("bonus"),
                        race_id=race.id
                    )
                skill_model.save()

            if players_data[key_name].get("guild"):
                if Guild.objects.filter(
                        name=players_data[key_name].get("guild").get("name")
                ).exists():
                    guild = Guild.objects.filter(
                        name=players_data[key_name].get("guild").get("name")
                    )[0]

                else:
                    guild = Guild(
                        name=players_data[key_name].get("guild").get("name"),
                        description=players_data[key_name].get(
                            "guild"
                        ).get("description")
                    )
                guild.save()
            else:
                guild = None

            player = Player(
                nickname=key_name,
                email=players_data[key_name].get("email"),
                bio=players_data[key_name].get("bio"),
                race=race,
                guild=guild,

            )
            player.save()


if __name__ == "__main__":
    main()
