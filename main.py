import json
import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild


def create_new_user(
        player: str,
        players_inf: dict,
        guild: Guild,
        race: Race
) -> None:
    Player.objects.create(
        nickname=player,
        email=players_inf["email"],
        bio=players_inf["bio"],
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
    for player, players_inf in players.items():
        race_inf = players_inf["race"]
        race = get_or_crate_race(race_inf)
        get_or_create_skills(race_inf["skills"], race)
        guild = get_or_create_guild(players_inf)
        create_new_user(player, players_inf, guild, race)


if __name__ == "__main__":
    main()
