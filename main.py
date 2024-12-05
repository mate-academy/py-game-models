import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with (open("players.json", "r") as file):
        players = json.load(file)
    for player, player_info in players.items():
        race, created = Race.objects.get_or_create(
            name=player_info["race"]["name"],
            description=player_info["race"]["description"])
        for skill_ in player_info["race"]["skills"]:
            skill, created = Skill.objects.get_or_create(
                name=skill_["name"],
                bonus=skill_["bonus"],
                race=race)

        guild = None
        if player_info.get("guild"):
            guild, created = Guild.objects.get_or_create(
                name=player_info["guild"]["name"],
                description=player_info["guild"]["description"])

        player_, created = Player.objects.get_or_create(
            nickname=player,
            email=player_info["email"],
            bio=player_info["bio"],
            race=race,
            guild=guild)


if __name__ == "__main__":
    main()
