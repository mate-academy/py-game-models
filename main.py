import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild
from json import load
from django.db import transaction


def main() -> None:

    with open("players.json") as file:
        data = load(file)

    for nickname, player_data in data.items():
        with transaction.atomic():
            race_data = player_data.pop("race")
            skills_data = race_data.pop("skills", [])

            race, _ = Race.objects.get_or_create(
                name=race_data["name"],
                defaults={"description": race_data["description"]}
            )

            for skill in skills_data:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    race=race,
                    defaults={"bonus": skill["bonus"]}
                )

            guild_data = player_data.get("guild") or None

            guild = None
            if guild_data:
                guild, _ = Guild.objects.get_or_create(
                    name=guild_data["name"],
                    defaults={"description": guild_data["description"]}
                )

            Player.objects.update_or_create(
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
