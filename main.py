import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:

    # Read data from the file.
    with open("players.json", "r") as file:
        data = json.load(file)

    for nickname, info in data.items():

        # getting or creating player's race
        raw_race = info.get("race")
        race = Race.objects.get_or_create(
            name=raw_race.get("name"),
            description=raw_race.get("description")
        )[0]

        # getting or creating skills of the race
        raw_skills = raw_race.get("skills")
        for raw_skill in raw_skills:
            Skill.objects.get_or_create(
                name=raw_skill.get("name"),
                bonus=raw_skill.get("bonus"),
                race=race
            )

        # if player in the guild getting or creating one
        guild = None
        raw_guild = info.get("guild")
        if raw_guild is not None:
            guild = Guild.objects.get_or_create(
                name=raw_guild.get("name"),
                description=raw_guild.get("description")
            )[0]

        # creating the player
        Player.objects.create(
            nickname=nickname,
            email=info.get("email"),
            bio=info.get("bio"),
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
