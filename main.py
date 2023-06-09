import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players_data = json.load(file)

    for nick_name, player in players_data.items():
        new_guild = None
        race_name = player["race"]["name"]
        race_description = player["race"]["description"]
        if not Race.objects.filter(name=race_name).exists():
            new_race = Race(name=race_name, description=race_description)
            new_race.save()
        else:
            new_race = Race.objects.get(name=race_name)
        if player["guild"]:
            guild_name = player["guild"]["name"]
            guild_description = player["guild"]["description"]
            if not Guild.objects.filter(name=guild_name).exists():
                new_guild = Guild(
                    name=guild_name,
                    description=guild_description
                )
                new_guild.save()
            else:
                new_guild = Guild.objects.get(name=guild_name)
        if player["race"]["skills"]:
            for skill in player["race"]["skills"]:
                skill_name = skill["name"]
                skill_bonus = skill["bonus"]
                if not Skill.objects.filter(name=skill_name).exists():
                    new_skill = Skill(
                        name=skill_name,
                        bonus=skill_bonus,
                        race=new_race
                    )
                    new_skill.save()

        new_player = Player(
            nickname=nick_name,
            email=player["email"],
            bio=player["bio"],
            race=new_race,
            guild=new_guild
        )
        new_player.save()


if __name__ == "__main__":
    main()
