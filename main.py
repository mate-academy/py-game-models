import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    Guild.objects.all().delete()
    Race.objects.all().delete()
    with open("players.json", "r") as file:
        data = json.load(file)
        for name in data:
            player_data = data[name]
            player_race = player_data["race"]
            player_guild = player_data["guild"]
            if player_guild:
                player_guild, _ = Guild.objects.get_or_create(
                    **player_guild)
            if player_race:
                race_skills = player_race.pop("skills")
                player_race, _ = Race.objects.get_or_create(
                    **player_race)
                for skill in race_skills:
                    Skill.objects.get_or_create(**skill, race=player_race)

            player_data.pop("race")
            player_data.pop("guild")
            # print(player_data, 'player data')
            # print(player_race, 'player_race')
            # print(player_guild, 'player_guild')
            Player.objects.create(
                **player_data, nickname=name,
                race=player_race,
                guild=player_guild
            )


if __name__ == "__main__":
    main()
