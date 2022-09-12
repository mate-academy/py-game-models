import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main():
    with open("players.json", "r") as f:
        json_data = json.load(f)
        print(json_data)
        for json_player in json_data:
            json_race = json_data[json_player]["race"]
            json_skills = json_race["skills"]
            json_guild = json_data[json_player]["guild"]
            if not Race.objects.filter(name=json_race["name"]).exists():
                race = Race(name=json_race["name"],
                            description=json_race["description"])
                race.save()
            race = Race.objects.get(name=json_race["name"])
            for json_skill in json_skills:
                if not Skill.objects.filter(name=json_skill["name"]).exists():
                    skill = Skill(
                        name=json_skill["name"],
                        bonus=json_skill["bonus"],
                        race=race
                    )
                    skill.save()
            if json_guild is None:
                guild = None
            elif not Guild.objects.filter(name=json_guild["name"]).exists():
                guild = Guild(
                    name=json_guild["name"],
                    description=json_guild["description"]
                )
                guild.save()
            else:
                guild = Guild.objects.filter(name=json_guild["name"]).all()[0]
            if not Player.objects.filter(nickname=json_player).exists():
                player = Player(
                    nickname=json_player,
                    email=json_data[json_player]["email"],
                    bio=json_data[json_player]["bio"],
                    race=race,
                    guild=guild
                )
                player.save()


if __name__ == "__main__":
    main()
