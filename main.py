import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    races = {}
    guilds = {}
    skills = set()

    for nickname, data in players.items():
        race_data = data["race"]
        race_name = race_data["name"]

        if race_name not in races:
            races[race_name] = Race.objects.create(
                name=race_name,
                description=race_data.get("description") or "",
            )
        race = races[race_name]

        for skill_data in race_data.get("skills", []):
            if skill_data["name"] not in skills:
                Skill.objects.create(
                    name=skill_data["name"],
                    bonus=skill_data["bonus"],
                    race=race,
                )
                skills.add(skill_data["name"])

        guild = None
        guild_data = data.get("guild")
        if guild_data:
            guild_name = guild_data["name"]
            if guild_name not in guilds:
                guilds[guild_name] = Guild.objects.create(
                    name=guild_name,
                    description=guild_data.get("description"),
                )
            guild = guilds[guild_name]

        Player.objects.create(
            nickname=nickname,
            email=data["email"],
            bio=data["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
