import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    Race.objects.all().delete()
    Skill.objects.all().delete()
    Guild.objects.all().delete()
    Player.objects.all().delete()
    with open("players.json", "r") as f:
        json_data = json.load(f)
    players = json_data.items()
    for i, (nickname, details) in enumerate(players):
        race, _ = Race.objects.get_or_create(
            name=details["race"]["name"],
            defaults={"description": details["race"]["description"]}
        )
        guild = None
        if details.get("guild"):
            guild, _ = Guild.objects.get_or_create(
                name=details["guild"]["name"],
                defaults={"description": details["guild"]["description"]}
            )
        player = Player.objects.create(
            nickname=nickname,
            email=details["email"],
            bio=details["bio"],
            race=race,
            guild=guild
        )
        skills = details["race"].get("skills", [])
        for skill in skills:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )


if __name__ == "__main__":
    main()
