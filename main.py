import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data_form_json = json.load(file)

    for nickname, player_info in data_form_json.items():

        race, _ = Race.objects.get_or_create(
            name=player_info["race"]["name"],
            description=player_info["race"]["description"],
        )

        guild = None
        if player_info.get("guild"):
            guild, _ = Guild.objects.get_or_create(
                name=player_info["guild"]["name"],
                description=player_info["guild"].get("description"),
            )

        for skill in player_info["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race,
            )

        Player.objects.create(
            nickname=nickname,
            email=player_info["email"],
            bio=player_info["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
