import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild
import json


def main() -> None:
    with open("players.json", "r", encoding="utf-8") as file:
        players_data = json.load(file)

    for nickname, attributes in players_data.items():
        race_data = attributes.get("race")

        if race_data:
            race_obj, _ = Race.objects.get_or_create(
                name=race_data.get("name"),
                defaults={"description": race_data.get("description", "")}
            )
        else:
            race_obj = None

        skills_data = race_data.get("skills", []) if race_data else []

        for skill in skills_data:
            name = skill.get("name")
            bonus = skill.get("bonus")

            if name and bonus:
                Skill.objects.get_or_create(
                    name=name,
                    defaults={"bonus": bonus, "race": race_obj}
                )

        guild_data = attributes.get("guild")

        if guild_data:
            guild_obj, _ = Guild.objects.get_or_create(
                name=guild_data.get("name"),
                defaults={"description": guild_data.get("description")}
            )
        else:
            guild_obj = None

        Player.objects.create(
            nickname=nickname,
            email=attributes.get("email"),
            bio=attributes.get("bio", ""),
            race=race_obj,
            guild=guild_obj
        )


if __name__ == "__main__":
    main()
