import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with (open("players.json", "r") as file):
        players = json.load(file)
        for player in players:
            race, created = Race.objects.get_or_create(
                name=players[player]["race"]["name"],
                description=players[player]["race"]["description"])
            for skill_ in players[player]["race"]["skills"]:
                skill, created = Skill.objects.get_or_create(
                    name=skill_["name"],
                    bonus=skill_["bonus"],
                    race=race)
            try:
                guild, created = Guild.objects.get_or_create(
                    name=players[player]["guild"]["name"],
                    description=players[player]["guild"]["description"])
            except TypeError:
                guild = None
            player_, created = Player.objects.get_or_create(
                nickname=player,
                email=players[player]["email"],
                bio=players[player]["bio"],
                race=race,
                guild=guild)


if __name__ == "__main__":
    main()
