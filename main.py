import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    Guild.objects.all().delete()
    Race.objects.all().delete()
    data = {}
    with open("players.json", "r") as file:
        data = json.load(file)
    for player_name in data:
        player_data = data.get(player_name)
        player_race = player_data.get("race")
        player_guild = player_data.get("guild")
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
        Player.objects.create(
            **player_data, nickname=player_name,
            race=player_race,
            guild=player_guild
        )


if __name__ == "__main__":
    main()
