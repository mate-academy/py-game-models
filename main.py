import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    json_file_path = "players.json"

    with open(json_file_path, 'r') as file:
        data = json.load(file)

    for nickname, player_data in data.items():
        player = Player(
            nickname=nickname,
            email=player_data["email"],
            bio=player_data["bio"]
        )
        race, created = Race.objects.get_or_create(
            name=player_data["race"]["name"],
            defaults={'description': player_data["race"]["description"]}
        )
        for skill_data in player_data["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill_data["name"],
                defaults={'bonus': skill_data["bonus"], 'race': race}
            )
        guild = None
        if player_data.get("guild"):
            guild, created = Guild.objects.get_or_create(
                name=player_data["guild"]["name"],
                defaults={'description': player_data["guild"]["description"]}
            )
        player.race = race
        player.guild = guild
        player.save()


if __name__ == "__main__":
    Guild.objects.all().delete()
    Player.objects.all().delete()
    Race.objects.all().delete()
    Skill.objects.all().delete()
    main()
