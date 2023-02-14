import json
import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild


def create_new_user(
        players: dict,
        player: dict,
        guild: Guild,
        race: Race
) -> None:
    Player.objects.create(
        nickname=player,
        email=players[player]["email"],
        bio=players[player]["bio"],
        race=race,
        guild=guild,
    )


def get_or_create_guild(pl_inf: dict) -> Guild:
    if pl_inf["guild"]:
        guild, created = Guild.objects.get_or_create(
            name=pl_inf["guild"]["name"],
            description=pl_inf["guild"]["description"]
        )
    else:
        guild = None
    return guild


def get_or_create_skills(skills: dict, race: Race) -> None:
    for skil_inf in skills:
        skil, created = Skill.objects.get_or_create(
            name=skil_inf["name"],
            bonus=skil_inf["bonus"], race=race
        )


def get_or_crate_race(race_inf: dict) -> Race:
    race, created = Race.objects.get_or_create(
        name=race_inf["name"],
        description=race_inf["description"]
    )
    return race


def main() -> None:
    with open("players.json") as players_inf:
        players = json.load(players_inf)
    for player in players:
        race_inf = players[player]["race"]
        race = get_or_crate_race(race_inf)
        get_or_create_skills(race_inf["skills"], race)
        guild = get_or_create_guild(players[player])
        create_new_user(players, player, guild, race)


if __name__ == "__main__":
    main()
