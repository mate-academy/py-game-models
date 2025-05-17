import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json",
              "r") as f:
        players_inf = json.load(f)
    for user, user_info in players_inf.items():
        race, _ = Race.objects.get_or_create(
            name=user_info["race"]["name"],
            description=user_info["race"]["description"]
        )
        for skill in user_info["race"].get("skills",
                                           []):
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )
        guild = None
        if user_info.get("guild"):
            guild, _ = Guild.objects.get_or_create(
                name=user_info["guild"]["name"],
                description=user_info["guild"]["description"]
            )
        Player.objects.create(
            nickname=user,
            email=user_info["email"],
            bio=user_info["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
