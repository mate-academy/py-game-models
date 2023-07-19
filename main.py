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

        race = info_race["name"]
        guild = None

        if not Race.objects.filter(name=race).exists():
            race = Race(
                name=race,
                description=info_race["description"]
            )
            race.save()
        else:
            race = Race.objects.get(name=race)

        if list_of_info_skills:
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

        if info_guild:
            if not Guild.objects.filter(name=info_guild["name"]).exists():
                guild = Guild(
                    name=info_guild["name"],
                    description=info_guild["description"]
                )
                guild.save()
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
