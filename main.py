import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as json_file:
        players = json.load(json_file)
    for nickname, player_data in players.items():
        race = Race.objects.get_or_create(
            name=player_data["race"]["name"],
            description=player_data["race"]["description"],
        )[0]
        race.save()
        for skill_info in player_data["race"]["skills"]:
            skill = Skill.objects.get_or_create(
                name=skill_info["name"],
                bonus=skill_info["bonus"],
                race=race
            )[0]
            skill.save()
        if player_data["guild"]:
            guild = Guild.objects.get_or_create(
                name=player_data["guild"]["name"],
                description=player_data["guild"]["description"]
            )[0]
            guild.save()
        else:
            guild = None
        player = Player.objects.get_or_create(
            nickname=nickname,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race,
            guild=guild
        )[0]
        player.save()


if __name__ == "__main__":
    main()
