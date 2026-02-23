import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data_players = json.load(file)

    for nickname, value in data_players.items():
        p_email = value["email"]
        p_bio = value["bio"]
        race, _ = Race.objects.get_or_create(
            name=value["race"]["name"],
            defaults={"description": value["race"]["description"]}
        )
        for sk_player in value["race"]["skills"]:
            Skill.objects.get_or_create(
                name=sk_player["name"],
                defaults={
                    "bonus": sk_player["bonus"],
                    "race": race
                }
            )
        guild = None
        if value["guild"] is not None:
            guild, _ = Guild.objects.get_or_create(
                name=value["guild"]["name"],
                defaults={"description": value["guild"]["description"]}
            )

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": p_email,
                "bio": p_bio,
                "race": race,
                "guild": guild
            }
        )


if __name__ == "__main__":
    main()
