import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players_data = json.load(file)

    for player_nick, player_dict in players_data.items():
        race, created = Race.objects.get_or_create(
            name=player_dict["race"]["name"],
            defaults={"description": player_dict["race"]["description"]}
        )
        for race_skill in player_dict["race"]["skills"]:
            Skill.objects.get_or_create(
                name=race_skill["name"],
                bonus=race_skill["bonus"],
                race=race
            )
        guild = None
        if player_dict.get("guild"):
            guild, created = Guild.objects.get_or_create(
                name=player_dict["guild"]["name"],
                defaults={
                    "description": player_dict["guild"].get("description")
                }
            )
        player, created = Player.objects.get_or_create(
            nickname=player_nick,
            defaults={"email": player_dict["email"],
                      "bio": player_dict["bio"],
                      "race": race,
                      "guild": guild
                      }
        )


if __name__ == "__main__":
    main()
