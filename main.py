import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as arquivo:
        players = json.load(arquivo)

    for player_name in players:
        player_dict = players[player_name]
        race_dict = player_dict["race"]

        try:
            race_obj = Race.objects.get(
                name=race_dict["name"],
                description=race_dict["description"]
            )
        except Race.DoesNotExist:
            race_obj = Race(
                name=race_dict["name"],
                description=race_dict["description"]
            )
            race_obj.save()

        skills_dict = player_dict["race"]["skills"]

        for skill_dict in skills_dict:
            try:
                skill_obj = Skill.objects.get(
                    name=skill_dict["name"],
                    bonus=skill_dict["bonus"],
                    race=race_obj
                )
            except Skill.DoesNotExist:
                skill_obj = Skill(
                    name=skill_dict["name"],
                    bonus=skill_dict["bonus"],
                    race=race_obj
                )
                skill_obj.save()

        guild_dict = player_dict["guild"]

        if guild_dict is None:
            guild_obj = None
        else:
            try:
                guild_obj = Guild.objects.get(**guild_dict)
            except Guild.DoesNotExist:
                guild_obj = Guild(**guild_dict)
                guild_obj.save()

        player_obj = Player(
            nickname=player_name,
            email=player_dict["email"],
            bio=player_dict["bio"],
            race=race_obj,
            guild=guild_obj
        )
        player_obj.save()


if __name__ == "__main__":
    main()
