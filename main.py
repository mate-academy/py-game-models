import json
import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as players_inf:
        players = json.load(players_inf)
    for player in players:
        race_inf = players[player]["race"]
        race, created = Race.objects.get_or_create(
            name=race_inf["name"],
            description=race_inf["description"]
        )

        for skil_inf in race_inf["skills"]:
            skil, created = Skill.objects.get_or_create(
                name=skil_inf["name"],
                bonus=skil_inf["bonus"], race=race
            )
        if players[player]["guild"]:
            guild, created = Guild.objects.get_or_create(
                name=players[player]["guild"]["name"],
                description=players[player]["guild"]["description"]
            )
        else:
            guild = None

        Player.objects.create(
            nickname=player,
            email=players[player]["email"],
            bio=players[player]["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
