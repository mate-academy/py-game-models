import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        player_data = json.load(file)

    for nickname, data in player_data.items():
        guild = None
        race, _ = Race.objects.get_or_create(
            name=data["race"]["name"],
            description=data["race"]["description"]
        )
        for skill_data in data["race"]["skills"]:
            skill, _ = Skill.objects.get_or_create(
                name=skill_data["name"],
                bonus=skill_data["bonus"],
                race=race
            )
        if data["guild"]:
            guild, _ = Guild.objects.get_or_create(
                name=data["guild"]["name"],
                description=data["guild"]["description"]
            )
        player, _ = Player.objects.get_or_create(
            nickname=nickname,
            email=data["email"],
            bio=data["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
