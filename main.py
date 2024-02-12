import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for player in players.items():

        player_race, _ = Race.objects.get_or_create(
            name=player[1]["race"]["name"],
            description=player[1]["race"]["description"])

        if race_skills := player[1]["race"]["skills"]:
            for skill in race_skills:
                Skill.objects.get_or_create(
                    **skill,
                    race=player_race
                )
        if guilds := player[1]["guild"]:
            guilds, _ = Guild.objects.get_or_create(
                **guilds
            )

        Player.objects.get_or_create(
            nickname=player[0],
            email=player[1]["email"],
            bio=player[1]["bio"],
            race=player_race,
            guild=guilds,
        )
    pass


if __name__ == "__main__":
    main()
