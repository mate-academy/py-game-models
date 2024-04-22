import json
import init_django_orm  # noqa: F401


from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file_json:
        data = json.load(file_json)
    for nickname, player_data in data.items():
        race, _ = Race.objects.get_or_create(
            name=player_data["race"]["name"],
            defaults={"description": player_data["race"]["description"]}
        )

        for skill_data in player_data["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill_data["name"],
                defaults={
                    "bonus": skill_data["bonus"],
                    "race_id": race.id
                }
            )
        guild = None
        if player_data["guild"]:
            guild, _ = Guild.objects.get_or_create(
                name=player_data["guild"]["name"],
                defaults={
                    "description": player_data["guild"]["description"]
                }
            )

        Player.objects.filter(nickname=nickname).get_or_create(
            nickname=nickname,
            defaults={
                "email": player_data["email"],
                "bio": player_data["bio"],
                "race": race,
                "guild": guild
            }
        )


if __name__ == "__main__":
    main()
