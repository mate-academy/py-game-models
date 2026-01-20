import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        player_info = json.load(file)

    for player in player_info:
        race, _ = Race.objects.get_or_create(
            name=player_info[player]["race"]["name"],
            description=player_info[player]["race"]["description"]
        )

        for skill_info in player_info[player]["race"]["skills"]:
            skill, _ = Skill.objects.get_or_create(
                name=skill_info["name"],
                bonus=skill_info["bonus"],
                race=race
            )

        guild = None
        if player_info[player]["guild"]:
            guild, _ = Guild.objects.get_or_create(
                name=player_info[player]["guild"]["name"],
                description=player_info[player]["guild"]["description"]
            )

        Player.objects.create(
            nickname=player,
            email=player_info[player]["email"],
            bio=player_info[player]["bio"],
            guild=guild,
            race=race
        )


if __name__ == "__main__":
    Race.objects.all().delete()
    Skill.objects.all().delete()
    Player.objects.all().delete()
    Guild.objects.all().delete()
    main()
