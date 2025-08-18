import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("./players.json", "r") as f:
        players = json.load(f)
    for player in players:
        Player.objects.create(
            nickname=player,
            email=player.get("email"),
            bio=player.get("bio"),
            race=Race.objects.get_or_create(
                name=player.get("race").get("name"),
                defaults={"description":player.get("race").get("description")}
            )[0],
            skills = [Skill.objects.get_or_create(
                name = skill.get("name"),
                defaults={
                    "bonus": skill.get("bonus"),
                    "race": Race.objects.get(
                        name=player.get("race").get("name")
                    )
                }
            )[0] for skill in player.get("skills")],
            guild=Guild.objects.get_or_create(
                name=player.get("guild").get("name", None),
                defaults={"description":player.get("guild").get("description")}
            )[0]
        )


if __name__ == "__main__":
    main()
