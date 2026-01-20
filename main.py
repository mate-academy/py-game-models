import json
from django.db.utils import IntegrityError

import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for nickname, player in players.items():
        race_obj, _ = Race.objects.get_or_create(
            name=player["race"]["name"],
            defaults={"description": player["race"]["description"]}
        )

        guild_obj = None
        if player["guild"]:
            guild_obj, _ = Guild.objects.get_or_create(
                name=player["guild"]["name"],
                defaults={"description": player["guild"]["description"]}
            )

        try:
            player_obj, _ = Player.objects.get_or_create(
                nickname=nickname,
                defaults={
                    "email": player["email"],
                    "bio": player["bio"],
                    "race": race_obj,
                    "guild": guild_obj  # Guild може бути None
                }
            )
        except IntegrityError as e:
            print(f"Помилка при створенні гравця {nickname}: {e}")
            continue

        for skill in player["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                defaults={"bonus": skill["bonus"], "race": race_obj}
            )


if __name__ == "__main__":
    main()
