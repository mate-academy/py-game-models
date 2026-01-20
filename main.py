import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild
import json as js


def main() -> None:
    with open("players.json", "r") as read_file:
        data = js.load(read_file)

    for name, values in data.items():

        if values.get("race"):
            race, _ = Race.objects.get_or_create(
                name=values.get("race").get("name", ""),
                description=values.get("race").get("description", ""))

        if values.get("guild"):
            guild, _ = Guild.objects.get_or_create(
                name=values.get("guild", "").get("name", ""),
                defaults={
                    "description": values.get("guild").get("description", "")
                }
            )
        else:
            guild = None
        player, _ = Player.objects.get_or_create(
            nickname=name,
            defaults={"email": values.get("email", ""),
                      "bio": values.get("bio", ""),
                      "race": race,
                      "guild": guild
                      }
        )

        for skll in values.get("race").get("skills"):
            skill, _ = Skill.objects.get_or_create(
                name=skll.get("name"),
                defaults={"bonus": skll.get("bonus"),
                          "race": race
                          }
            )


if __name__ == "__main__":
    main()
