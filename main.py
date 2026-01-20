import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as f:
        data = json.load(f)

    Skill.objects.all().delete()
    Player.objects.all().delete()
    Guild.objects.all().delete()
    Race.objects.all().delete()

    races = {}
    guilds = {}

    for nickname, player_data in data.items():
        race_name = player_data["race"]["name"]
        if race_name not in races:
            race = Race.objects.create(
                name=race_name,
                description=player_data["race"]["description"]
            )
            races[race_name] = race

            for skill_data in player_data["race"]["skills"]:
                Skill.objects.create(
                    name=skill_data["name"],
                    bonus=skill_data["bonus"],
                    race=race
                )
        else:
            race = races[race_name]

        guild = None
        if player_data.get("guild"):
            guild_name = player_data["guild"]["name"]
            if guild_name not in guilds:
                guild = Guild.objects.create(
                    name=guild_name,
                    description=player_data["guild"]["description"]
                )
                guilds[guild_name] = guild
            else:
                guild = guilds[guild_name]

        Player.objects.create(
            nickname=nickname,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
