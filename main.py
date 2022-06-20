import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main():

    with open("players.json") as f:
        data = json.load(f)

    for name, description in data.items():

        # check if race exists
        race, _ = Race.objects.get_or_create(
            name=description["race"]["name"],
            description=description["race"]["description"]
        )

        # check_the_skills_exists
        for skill in description["race"]["skills"]:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(name=skill["name"],
                                     bonus=skill["bonus"],
                                     race=race)

        # check the guild exists
        if description["guild"]:
            guild, _ = Guild.objects.get_or_create(
                name=description["guild"]["name"],
                description=description["guild"]["description"]
            )
        else:
            guild = None

        # make a player
        Player.objects.create(nickname=name,
                              email=description["email"],
                              bio=description["bio"],
                              race=race,
                              guild=guild)


if __name__ == "__main__":
    main()
