import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        players = json.load(f)

    for nickname, data in players.items():
        data_race = data["race"]
        race, created = Race.objects.get_or_create(
            name=data_race["name"],
            defaults={"description": data_race.get("description")}
        )

        skills = data_race.get("skills")
        for skill in skills:
            Skill.objects.get_or_create(name=skill["name"],
                                        bonus=skill.get("bonus"),
                                        race=race)

        guild = data.get("guild")
        if guild:
            guild, created = Guild.objects.get_or_create(
                name=guild["name"],
                defaults={"description": guild.get("description")}
            )
        else:
            guild = None

        Player.objects.create(nickname=nickname, email=data["email"],
                              bio=data["bio"], race=race, guild=guild)


if __name__ == "__main__":
    main()
