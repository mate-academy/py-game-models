import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_file:
        players = json.load(players_file)

    def race_db_filler(player_data: dict) -> Race:
        player_race, _ = Race.objects.get_or_create(
            name=data.get("race").get("name"),
            description=data.get("race").get("description"),
        )
        return player_race

    def guild_db_filler(player_data: dict) -> Guild:
        player_guild = None
        if data.get("guild"):
            player_guild, _ = Guild.objects.get_or_create(
                name=data.get("guild").get("name"),
                description=data.get("guild").get("description"),
            )
        return player_guild

    def skill_db_filler(user_data: dict) -> None:
        for skill in user_data.get("race").get("skills", []):
            Skill.objects.get_or_create(
                name=skill.get("name"),
                bonus=skill.get("bonus"),
                race_id=race.id
            )

    def player_db_filler(player: dict) -> None:
        Player.objects.get_or_create(
            nickname=nickname,
            email=data.get("email"),
            bio=data.get("bio"),
            race=race,
            guild=guild
        )

    for nickname, data in players.items():
        race = race_db_filler(data)
        guild = guild_db_filler(data)
        skill_db_filler(data)
        player_db_filler(data)
