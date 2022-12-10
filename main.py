import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:

    # load information from json

    with open("players.json", "r") as f:
        players = json.load(f)
    for key, value in players.items():

        # create unique race

        race = Race(
            name=value["race"]["name"],
            description=value["race"]["description"]
        )
        if Race.objects.filter(name=value["race"]["name"]).exists() is False:
            race.save()

        # create skills

        for skill in value["race"]["skills"]:
            race_ = Race.objects.get(name=value["race"]["name"])
            skill_ = Skill(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race_
            )
            if Skill.objects.filter(name=skill["name"]).exists() is False:
                skill_.save()

        # create guilds

        if value["guild"] is not None:
            guild = Guild(
                name=value["guild"]["name"],
                description=value["guild"]["description"]
            )
            if Guild.objects.filter(
                    name=value["guild"]["name"]
            ).exists() is False:
                guild.save()

        # create players

        race_for_player = Race.objects.get(name=value["race"]["name"])
        guild_for_player = None
        if value["guild"] is not None:
            guild_for_player = Guild.objects.get(name=value["guild"]["name"])
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
