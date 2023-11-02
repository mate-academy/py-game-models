import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        players = json.load(f)

    for player in players:
        player_info = players[player]
        player_guild_info = player_info.get("guild")
        player_race_info = player_info.get("race")
        players_skills_info = player_race_info.get("skills")

        race_name = player_race_info.get("name")
        race_description = player_race_info.get("description")
        race, race_created = Race.objects.get_or_create(
            name=race_name,
            description=race_description
        )
        if players_skills_info:
            for skill in players_skills_info:
                skill_name = skill.get("name")
                skill_bonus = skill.get("bonus")
                Skill.objects.get_or_create(
                    name=skill_name,
                    bonus=skill_bonus,
                    race=race
                )

        if player_guild_info:
            guild, guild_created = Guild.objects.get_or_create(
                name=player_guild_info.get("name"),
                description=player_guild_info.get("description")
            )
        else:
            guild = None

        Player.objects.get_or_create(
            nickname=player,
            email=player_info.get("email"),
            bio=player_info.get("bio"),
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
