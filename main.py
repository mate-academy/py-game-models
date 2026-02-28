import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)
    for key, value in data.items():
        name = key
        email = value.get("email")
        bio = value.get("bio")
        race_name = value.get("race")["name"]
        race_description = value.get("race")["description"]
        skills = value.get("race", {}).get("skills", [])
        skills_dict = {n.get("name"): n.get("bonus") for n in skills}
        race, was_created =\
            Race.objects.get_or_create(name=race_name,
                                       defaults={"description":
                                                 race_description})
        for skill_name, skill_bonus in skills_dict.items():
            skill, was_created = Skill.objects.get_or_create(
                name=skill_name,
                race=race,
                defaults={"bonus": skill_bonus}
            )
        guild = None
        if value.get("guild") is not None:
            guild_name = value.get("guild")["name"]
            guild_description = value.get("guild")["description"]
            guild, was_created =\
                Guild.objects.get_or_create(
                    name=guild_name, defaults={"description" :
                                               guild_description})
        Player.objects.create(
            nickname=name,
            email=email,
            bio=bio,
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
