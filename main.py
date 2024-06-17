import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open('players.json') as file:
        players = json.load(file)
    for name, attributes in players.items():
        player = Player(
            nickname=name,
            email=attributes["email"],
            bio=attributes["bio"],
        )

        race = Race.objects.get_or_create(
            name=attributes["race"]["name"],
            description=attributes["race"]["description"],
        )
        player.race = race[0]

        for skill_attributes in attributes["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill_attributes["name"],
                bonus=skill_attributes["bonus"],
                race=race[0]
            )

        if attributes.get("guild") is not None:
            guild = Guild.objects.get_or_create(
                name=attributes["guild"]["name"],
                description=attributes["guild"]["description"]
            )
            player.guild = guild[0]
        player.save()


if __name__ == "__main__":
    main()
