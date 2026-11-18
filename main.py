import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild
import json


def main() -> None:
    with open("players.json", encoding="utf-8") as file:
        data = json.load(file)

    for nickname, player in data.items():
        race_data = player["race"]

        race, _ = Race.objects.get_or_create(name=race_data["name"], defaults={
            "description": race_data["description"]}, )

        for skill_data in race_data["skills"]:
            skill_name = skill_data["name"]

            skill, _ = Skill.objects.get_or_create(name=skill_name, defaults={
                "bonus": skill_data["bonus"], "race": race, })

        guild_data = player.get("guild")
        guild = None

        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data["description"]}
            )

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": player["email"],
                "bio": player["bio"],
                "race": race, "guild": guild}
        )


if __name__ == "__main__":
    main()
