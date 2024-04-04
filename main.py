import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as f:
        data = json.load(f)

        guilds = {}
        races = {}
        for player in data.keys():
            # Create guilds
            if "guild" in data[player] and data[player]["guild"] is not None:
                guild_name = data[player]["guild"]["name"]
                if guild_name not in guilds:
                    guilds[guild_name] = Guild.objects.create(
                        name=guild_name,
                        description=data[player]["guild"]["description"],
                    )

            # Create races and skills
            race_name = data[player]["race"]["name"]
            if race_name not in races:
                races[race_name] = Race.objects.create(
                    name=race_name,
                    description=data[player]["race"]["description"],
                )
                if "skills" in data[player]["race"]:
                    for skill in data[player]["race"]["skills"]:
                        Skill.objects.create(
                            name=skill["name"],
                            bonus=skill["bonus"],
                            race=races[race_name]
                        )

            # Create players
            guild = guilds.get(
                data[
                    player]["guild"]["name"]
            )if "guild" in data[
                player] and data[
                player]["guild"] is not None else None
            race = races[data[player]["race"]["name"]]
            Player.objects.create(
                nickname=player,
                email=data[player]["email"],
                bio=data[player]["bio"],
                race=race,
                guild=guild,
            )


if __name__ == "__main__":
    main()
