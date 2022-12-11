import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        players = json.load(f)
    for nickname, player_info in players.items():
        race_name = player_info["race"]
        race = Race(
            name=race_name["name"],
            description=race_name["description"]
        )
        if Race.objects.filter(name=race_name["name"]).exists() is False:
            race.save()
        for skill in race_name["skills"]:
            race_ = Race.objects.get(name=race_name["name"])
            skill_ = Skill(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race_
            )
            if Skill.objects.filter(name=skill["name"]).exists() is False:
                skill_.save()
        guild_ = player_info["guild"]
        if guild_ is not None:
            guild = Guild(
                name=guild_["name"],
                description=guild_["description"]
            )
            if Guild.objects.filter(
                    name=guild_["name"]
            ).exists() is False:
                guild.save()
        race_for_player = Race.objects.get(name=race_name["name"])
        guild_for_player = Guild.objects.get(name=guild_["name"]) \
            if guild_ is not None else None
        player_ = Player(
            nickname=nickname,
            email=player_info["email"],
            bio=player_info["bio"],
            race=race_for_player,
            guild=guild_for_player
        )
        player_.save()


if __name__ == "__main__":
    main()
