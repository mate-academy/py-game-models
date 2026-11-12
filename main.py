import init_django_orm  # noqa: F401
import json


from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        data = json.load(f)

    for nickname, other in data.items():
        race, created = Race.objects.get_or_create(
            name=other.get("race")["name"],
            defaults={"description": other.get("race")["description"]})
        for skill in other.get("race")["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                defaults={"bonus": skill["bonus"], "race": race})
        guild = None
        if other.get("guild"):
            guild, created = Guild.objects.get_or_create(
                name=other.get("guild")["name"],
                defaults={"description": other.get("guild")["description"]}
            )

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": other["email"],
                "bio": other["bio"],
                "race": race,
                "guild": guild,
            }
        )


if __name__ == "__main__":
    main()
