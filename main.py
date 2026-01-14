import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    Race.objects.all().delete()
    Skill.objects.all().delete()
    Guild.objects.all().delete()
    Player.objects.all().delete()
    with open("players.json", "r") as file:
        players = json.load(file)
    for name in players:
        race = players[name].get("race", {})
        guild = players[name].get("guild", {})
        skills = race.get("skills", [])
        players_race = Race.objects.get_or_create(
            name=race.get("name", ""),
            description=race.get("description", ""),
        )[0]
        Player.objects.create(
            nickname=name,
            email=players[name].get("email"),
            bio=players[name].get("bio"),
            race=players_race,
            guild=Guild.objects.get_or_create(
                name=guild["name"]
                if guild else "unknown",
                description=guild["description"]
                if guild else ""
            )[0]
        )
        for skill in skills:
            Skill.objects.get_or_create(
                name=skill.get("name", ""),
                bonus=skill.get("bonus", ""),
                race=players_race
            )
        Guild.objects.filter(
            name="unknown"
        ).delete()


if __name__ == "__main__":
    main()
