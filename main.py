import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players = json.load(file)

    for nickname, data in players.items():
        race, _ = Race.objects.get_or_create(
            name=data.get("race").get("name"),
            description=data.get("race").get("description")
        )

        for skill in data.get("race").get("skills"):
            Skill.objects.get_or_create(
                name=skill.get("name"),
                bonus=skill.get("bonus"),
                race=race
            )

        player_guild = data.get("guild") if data.get("guild") else None
        if player_guild:
            player_guild, _ = Guild.objects.get_or_create(
                name=data.get("guild").get("name"),
                description=data.get("guild").get("description", "")
            )

        Player.objects.get_or_create(
            nickname=nickname,
            email=data.get("email"),
            bio=data.get("bio"),
            race=race,
            guild=player_guild
        )


if __name__ == "__main__":
    main()
