import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    create_race_entries(players)
    create_skills_entries(players)
    create_guild_entries(players)
    create_player_entries(players)


def create_race_entries(players: dict) -> None:
    for player in players:
        race = players.get(player).get("race")
        description = (
            race.get("description") if race.get("description") else None
        )
        Race.objects.get_or_create(
            name=race.get("name"),
            description=description
        )


def create_skills_entries(players: dict) -> None:
    for player in players:
        race = players.get(player).get("race")
        for skill in race.get("skills"):
            Skill.objects.get_or_create(
                name=skill.get("name"),
                bonus=skill.get("bonus"),
                race_id=Race.objects.get(name=race.get("name")).id
            )


def create_guild_entries(players: dict) -> None:
    for player in players:
        guild = players.get(player).get("guild")
        if guild:
            description = (
                guild.get("description")
                if guild.get("description")
                else None
            )
            Guild.objects.get_or_create(
                name=guild.get("name"),
                description=description
            )


def create_player_entries(players: dict) -> None:
    for player in players:
        race = players.get(player).get("race")
        guild = players.get(player).get("guild")
        guild_id = (
            Guild.objects.get(name=guild.get("name")).id
            if guild else None
        )
        race_id = Race.objects.get(name=race.get("name")).id
        Player.objects.get_or_create(
            nickname=player,
            email=players.get(player).get("email"),
            bio=players.get(player).get("bio"),
            race_id=race_id,
            guild_id=guild_id
        )


if __name__ == "__main__":
    main()
