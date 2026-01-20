import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r", encoding="utf-8") as file:
        players_data = json.load(file)
        for player in players_data.values():
            print(player)
            race, _ = Race.objects.get_or_create(
                name=player["race"]["name"],
                defaults={"description":
                          player["race"].get("description", "")})
            for skill_data in player["race"]["skills"]:
                Skill.objects.get_or_create(
                    name=skill_data["name"],
                    bonus=skill_data["bonus"],
                    race=race,
                )
            guild = None
            if player.get("guild"):
                guild, _ = Guild.objects.get_or_create(
                    name=player["guild"]["name"],
                    defaults={"description": player["guild"]
                              .get("description", "")}
                )
            guild = None
            nickname = player["email"].split("@")[0]
            Player.objects.get_or_create(
                nickname=nickname,
                defaults={"email": player["email"],
                          "bio": player.get("bio", ""),
                          "race": race,
                          "guild": guild,
                          }
            )


if __name__ == "__main__":
    main()
