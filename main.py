import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players: dict = json.load(file)

    for nickname, personal_info in players.items():
        race, created = Race.objects.get_or_create(
            name=personal_info["race"]["name"],
            description=personal_info["race"]["description"]
        )

        for skill in personal_info["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )

        guild = None
        if personal_info.get("guild"):
            guild, created = Guild.objects.get_or_create(
                name=personal_info["guild"]["name"],
                description=personal_info["guild"]["description"]
            )

        Player.objects.get_or_create(
            nickname=nickname,
            email=personal_info["email"],
            bio=personal_info["bio"],
            race=race,
            guild=guild,

        )


if __name__ == "__main__":
    main()
