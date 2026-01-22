import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as f:
        data = json.load(f)

    for player, info in data.items():
        race_data = info.get("race", {})
        race_instance, _ = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data["description"]}
        )
        guild = None
        if info.get("guild"):
            guild, _ = Guild.objects.get_or_create(
                name=info["guild"]["name"],
                defaults={"description": info["guild"]["description"]}
            )

        for skill in info["race"].get("skills", []):
            skill_instance, _ = Skill.objects.get_or_create(
                name=skill["name"],
                defaults={"bonus": skill["bonus"], "race": race_instance}
            )

        player_instance, _ = Player.objects.get_or_create(
            nickname=player,
            defaults={
                "email": info.get("email"),
                "bio": info.get("bio"),
                "race": race_instance,
                "guild": guild
            }
        )
        print(player_instance)


if __name__ == "__main__":
    main()
