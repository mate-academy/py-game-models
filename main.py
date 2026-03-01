import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        players_set = json.load(f)

    for nickname, info_user in players_set.items():

        # -------- RACE --------
        race, _ = Race.objects.get_or_create(
            name=info_user["race"]["name"],
            defaults={
                "description": info_user["race"].get("description", "")
            }
        )

        # -------- SKILLS --------
        for skill in info_user["race"].get("skills", []):
            Skill.objects.get_or_create(
                name=skill["name"],
                defaults={
                    "bonus": skill["bonus"],
                    "race": race
                }
            )

        # -------- GUILD --------
        guild = None
        if info_user.get("guild"):
            guild, _ = Guild.objects.get_or_create(
                name=info_user["guild"]["name"],
                defaults={
                    "description": info_user["guild"].get("description")
                }
            )

        # -------- PLAYER --------
        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": info_user["email"],
                "bio": info_user["bio"],
                "race": race,
                "guild": guild
            }
        )


if __name__ == "__main__":
    main()
