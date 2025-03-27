import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    file_name = "players.json"
    players = {}
    with open(file_name) as file_obj:
        players = json.load(file_obj)

    if players:
        for player_name, player in players.items():
            new_player = Player(
                nickname=player_name,
                email=player["email"],
                bio=player["bio"]
            )

            race = player["race"]
            new_race = Race(name=race["name"], description=race["description"])
            if not Race.objects.filter(name=new_race.name).exists():
                new_race.save()
            else:
                new_race = Race.objects.get(name=new_race.name)
            new_player.race = new_race

            skills = race["skills"]
            for skill in skills:
                new_skill = Skill(name=skill["name"], bonus=skill["bonus"])
                new_skill.race = new_race
                if not Skill.objects.filter(name=new_skill.name).exists():
                    new_skill.save()

            guild = player["guild"]
            if guild is not None:
                new_guild = Guild(
                    name=guild["name"], description=guild["description"]
                )
                if not Guild.objects.filter(name=new_guild.name).exists():
                    new_guild.save()
                else:
                    new_guild = Guild.objects.get(name=new_guild.name)
                new_player.guild = new_guild

            if not Player.objects.filter(
                    nickname=new_player.nickname
            ).exists():
                new_player.save()


if __name__ == "__main__":
    main()
