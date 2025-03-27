import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as json_file:
        players = json.load(json_file)
        for player in players:
            email, bio, player_race, player_guild = players[player].values()
            race_skills = player_race.get("skills")

            race, _ = Race.objects.get_or_create(
                name=player_race.get("name"),
                description=player_race.get("description"),
            )

            for skill in race_skills:
                Skill.objects.get_or_create(
                    name=skill.get("name"),
                    bonus=skill.get("bonus"),
                    race=race,
                )

            guild = None
            if player_guild:
                guild, _ = Guild.objects.get_or_create(
                    name=player_guild.get("name"),
                    description=player_guild.get("description"),
                )

            Player.objects.create(
                nickname=player,
                email=email,
                bio=bio,
                race=race,
                guild=guild
            )


if __name__ == "__main__":
    main()
