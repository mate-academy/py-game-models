import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        players = json.load(f)
    for key, value in players.items():
        race_name = value["race"]["name"]
        race = Race(
            name=race_name,
            description=value["race"]["description"]
        )
        if Race.objects.filter(name=race_name).exists() is False:
            race.save()
        for skill in value["race"]["skills"]:
            race_ = Race.objects.get(name=race_name)
            skill_ = Skill(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race_
            )
            if Skill.objects.filter(name=skill["name"]).exists() is False:
                skill_.save()
        if value["guild"] is not None:
            guild = Guild(
                name=value["guild"]["name"],
                description=value["guild"]["description"]
            )
            if Guild.objects.filter(
                    name=value["guild"]["name"]
            ).exists() is False:
                guild.save()
        race_for_player = Race.objects.get(name=race_name)
        guild_for_player = Guild.objects.get(name=value["guild"]["name"]) \
            if value["guild"] is not None else None
        player_ = Player(
            nickname=key,
            email=value["email"],
            bio=value["bio"],
            race=race_for_player,
            guild=guild_for_player
        )
        player_.save()


if __name__ == "__main__":
    main()
