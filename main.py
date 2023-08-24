import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as players:
        players_data = json.load(players)

    for player_nickname, player_attributes in players_data.items():
        race, created = Race.objects.get_or_create(
            name=player_attributes["race"]["name"],
            description=player_attributes["race"]["description"]
        )
        if created:
            for skill in player_attributes["race"].get("skills", []):
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )

        if player_attributes.get("guild"):
            guild, created = Guild.objects.get_or_create(
                name=player_attributes["guild"]["name"],
                description=player_attributes["guild"]["description"]
            )
        else:
            guild = None

        player, created = Player.objects.get_or_create(
            nickname=player_nickname,
            email=player_attributes["email"],
            bio=player_attributes["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
