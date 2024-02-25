import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild



def main() -> None:
    races = []
    with open("players.json") as player:
        players = json.load(player)
    for player_nick, player_info in players.items():
        email, bio, race_inf, guild_inf = player_info.values()
        race_index, _ = Race.objects.get_or_create(
            name=race_inf["name"],
            description=race_inf["description"]
        )
        skill_info = race_inf["skills"]
        for skill in skill_info:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race_index
            )
        if guild_inf:
            name_of_gild, desc = guild_inf.values()
            guild_index, _ = Guild.objects.get_or_create(
                name=name_of_gild,
                description=desc
            )
        else:
            guild_index = None
        Player.objects.get_or_create(
            nickname=player_nick,
            email=email,
            bio=bio,
            race=race_index,
            guild=guild_index
        )

if __name__ == "__main__":
    Race.objects.all().delete()
    Skill.objects.all().delete()
    Guild.objects.all().delete()
    Player.objects.all().delete()
    main()


