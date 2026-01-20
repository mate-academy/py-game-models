import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    Race.objects.all().delete()
    Skill.objects.all().delete()
    Player.objects.all().delete()
    Guild.objects.all().delete()
    with open("players.json", "r") as file:
        players = json.load(file)

    for player in players:
        user = players[player]
        race = user["race"]
        Race.objects.get_or_create(
            name=race["name"],
            description=race["description"]
        )

        character = Player(
            nickname=player,
            email=user["email"],
            bio=user["bio"],
            race=Race.objects.get(name=race["name"]),
        )

        guild = user.get("guild")
        if guild:
            Guild.objects.get_or_create(
                name=guild["name"],
                description=guild["description"]
            )
            character.guild = Guild.objects.get(name=guild["name"])
        character.save()

        skill_exists = user["race"].get("skills")
        if skill_exists:
            for skill in skill_exists:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=Race.objects.get(name=race["name"])
                )


if __name__ == "__main__":
    main()
