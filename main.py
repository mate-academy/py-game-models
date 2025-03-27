import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players = json.load(file)

    for player, details in players.items():

        race, _ = Race.objects.get_or_create(
            name=details["race"]["name"],
            defaults={"description": details["race"]["description"]}
        )

        guild = None
        if details["guild"] and details["guild"]["name"]:
            guild, _ = Guild.objects.get_or_create(
                name=details["guild"]["name"],
                defaults={"description": details["guild"]["description"]
                          or None}
            )

        for skills in details["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skills["name"],
                defaults={"bonus": skills["bonus"], "race": race}
            )

        Player.objects.get_or_create(
            nickname=player,
            defaults={"email": details["email"],
                      "bio": details["bio"],
                      "race": race, "guild": guild},
        )


if __name__ == "__main__":
    main()
