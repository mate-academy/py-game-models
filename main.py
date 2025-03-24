import json
import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        data_players = json.load(file)

    for player, data_player in data_players.items():
        race, _ = Race.objects.get_or_create(
            name=data_player["race"],
            defaults={"description": data_player["race"]["description"]}
        )

        guild = None
        if player_guild := data_player["guild"]:
            guild, _ = Guild.objects.get_or_create(
                name=player_guild["name"],
                defaults={"description": player_guild["description"]}
            )

        for skill_data in data_player["race"]["skills"]:
            skill_data, _ = Skill.objects.get_or_create(
                name=skill_data["name"],
                defaults={"bonus": skill_data["bonus"], "race": race}
            )

        Player.objects.get_or_create(
            nickname=player,
            defaults={
                "email": data_player["email"],
                "bio": data_player["bio"],
                "race": race,
                "guild": guild
            }
        )


if __name__ == "__main__":
    main()
