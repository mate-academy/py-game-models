import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)
    for name, date_player in players.items():
        race, flag_race_bool = Race.objects.get_or_create(
            name=date_player["race"]["name"],
            description=date_player["race"]["description"])
        if flag_race_bool:
            race.save()
        if date_player["race"]["skills"]:
            for skill in date_player["race"]["skills"]:
                skills, flag_skills = Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race)
                if flag_skills:
                    skills.save()
        if date_player["guild"]:
            guild, flag_guild = Guild.objects.get_or_create(
                name=date_player["guild"]["name"],
                description=date_player["guild"]["description"])
            if flag_guild:
                guild.save()
            Player.objects.get_or_create(
                nickname=name,
                email=date_player["email"],
                bio=date_player["bio"],
                race=race,
                guild=guild)
        else:
            Player.objects.get_or_create(
                nickname=name,
                email=date_player["email"],
                bio=date_player["bio"],
                race=race)


if __name__ == "__main__":
    main()
