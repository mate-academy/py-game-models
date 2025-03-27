import init_django_orm  # noqa: F401
import json


from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for player_name, player_info in data.items():

        race, created = Race.objects.get_or_create(
            name=player_info["race"]["name"],
            description=player_info["race"]["description"]
        )

        if created and player_info["race"].get("skills"):
            for skill in player_info["race"]["skills"]:
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )

        if player_info.get("guild"):
            guild, created = Guild.objects.get_or_create(
                name=player_info["guild"].get("name"),
                description=player_info["guild"].get("description")
            )
        else:
            guild = None

        Player.objects.create(
            nickname=player_name,
            email=player_info.get("email"),
            bio=player_info.get("bio"),
            guild=guild,
            race=race
        )


if __name__ == "__main__":
    main()
