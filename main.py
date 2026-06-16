import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)
    for nickname, info in data.items():
        race, _ = Race.objects.get_or_create(
            name=info["race"]["name"],
            defaults={"description": info["race"]["description"]}
        )

        guild_data = info.get("guild")
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=info["guild"]["name"],
                defaults={"description": info["guild"]["description"]}
            )
        else:
            guild = None

        for skill_info in info["race"]["skills"]:
            skill, _ = Skill.objects.get_or_create(
                name=skill_info["name"],
                defaults={"bonus": skill_info["bonus"], "race": race}
            )

        player, _ = Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": info["email"],
                "bio": info["bio"],
                "race": race,
                "guild": guild,
            }
        )


if __name__ == "__main__":
    main()
