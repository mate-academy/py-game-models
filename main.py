import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as f:
        data = json.load(f)

        guild_archers = Guild.objects.create(
            name=data["john"]["guild"]["name"],
            description=data["john"]["guild"]["description"],
        )
        guild_mags = Guild.objects.create(
            name=data["max"]["guild"]["name"],
            description=data["max"]["guild"]["description"],
        )
        guild_blacksmiths = Guild.objects.create(
            name=data["andrew"]["guild"]["name"],
            description=data["andrew"]["guild"]["description"],
        )
        race_elf = Race.objects.create(
            name=data["john"]["race"]["name"],
            description=data["john"]["race"]["description"],
        )
        race_human = Race.objects.create(
            name=data["nick"]["race"]["name"],
            description=data["nick"]["race"]["description"],
        )
        [Skill.objects.create(
            name=skill["name"],
            bonus=skill["bonus"],
            race=race_elf
        ) for skill in data["john"]["race"]["skills"]]

        for player in data.keys():
            guild = None
            if "guild" in data[player] and data[player]["guild"] is not None:
                if data[player]["guild"]["name"] == "archers":
                    guild = guild_archers
                elif data[player]["guild"]["name"] == "mags":
                    guild = guild_mags
                else:
                    guild = guild_blacksmiths
            race = (race_elf if data[player]["race"]["name"] == "elf"
                    else race_human)
            Player.objects.create(
                nickname=player,
                email=data[player]["email"],
                bio=data[player]["bio"],
                race=race,
                guild=guild,
            )


if __name__ == "__main__":
    main()
