import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players:
        players = json.load(players)
    for player, data in players.items():
        guild = data.get("guild")
        if guild:
            guild, _ = Guild.objects.get_or_create(
                name=data["guild"]["name"],
                defaults={"description": data["guild"]["description"]}
            )
        race, _ = Race.objects.get_or_create(
            name=data["race"]["name"],
            defaults={"description": data["race"]["description"]}
        )
        for skill_ in data["race"]["skills"]:
            skill, _ = Skill.objects.get_or_create(
                name=skill_["name"],
                defaults={"bonus": skill_["bonus"], "race": race}
            )
        player_, _ = Player.objects.get_or_create(
            nickname=player,
            defaults={
                "email": data["email"],
                "bio": data["bio"],
                "race": race,
                "guild": guild,
            }
        )


if __name__ == "__main__":
    main()
