import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_json:
        list_of_players = json.load(players_json)

    for name, info in list_of_players.items():
        info_race = info["race"]
        list_of_info_skills = info["race"]["skills"]
        info_guild = info["guild"]

        if not Race.objects.filter(name=info_race["name"]).exists():
            race = Race(
                name=info_race["name"],
                description=info_race["description"]
            )
            race.save()

        if len(list_of_info_skills) > 0:
            for skill_detail in list_of_info_skills:
                if not (
                    Skill.objects.filter(name=skill_detail["name"]).exists()
                ):
                    skill = Skill(
                        name=skill_detail["name"],
                        bonus=skill_detail["bonus"],
                        race=race,
                    )
                    skill.save()

        if info_guild is not None:
            if not Guild.objects.filter(name=info_guild["name"]).exists():
                guild = Guild(
                    name=info_guild["name"],
                    description=info_guild["description"]
                )
                guild.save()

        race = Race.objects.get(name=info_race["name"])
        guild = None

        if info_guild is None:
            guild = None
        else:
            guild = Guild.objects.get(name=info_guild["name"])

        player = Player(
            nickname=name,
            email=info["email"],
            bio=info["bio"],
            race=race,
            guild=guild
        )
        player.save()


if __name__ == "__main__":
    main()
