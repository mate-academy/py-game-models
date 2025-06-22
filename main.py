import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        data = json.load(f)

    for name in data.keys():
        race_name = data[name]["race"]["name"]
        race_description = data[name]["race"]["description"]

        Race.objects.get_or_create(
            name=race_name,
            description=race_description,
        )
        race_class = Race.objects.get(name=race_name)

        if data[name]["race"]["skills"]:
            for skill in data[name]["race"]["skills"]:
                skill_name = skill["name"]
                skill_bonus = skill["bonus"]
                Skill.objects.get_or_create(
                    name=skill_name,
                    bonus=skill_bonus,
                    race=race_class,
                )
        if data[name]["guild"] is not None:
            guild_name = data[name]["guild"]["name"]
            guild_description = data[name]["guild"]["description"]
            Guild.objects.get_or_create(
                name=guild_name,
                description=guild_description,
            )
            guild_class = Guild.objects.get(name=guild_name)
        else:
            guild_class = None

        Player.objects.get_or_create(
            nickname=name,
            email=data[name]["email"],
            bio=data[name]["bio"],
            race=race_class,
            guild=guild_class,
        )


if __name__ == "__main__":
    main()
