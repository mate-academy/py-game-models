import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:

    with open("players.json", "r") as file:
        data = json.load(file)

    for player, info in data.items():
        player_race = info["race"]
        skills = player_race.get("skills")
        guild = info.get("guild")

        if player_race:
            race, _ = Race.objects.get_or_create(
                name=info["race"]["name"],
                description=info["race"]["description"]
            )
            if skills:
                for skill in skills:
                    Skill.objects.get_or_create(name=skill["name"],
                                                bonus=skill["bonus"],
                                                race=race)
            if guild:
                guild, _ = Guild.objects.get_or_create(
                    name=guild["name"], description=guild["description"]
                )

        Player.objects.get_or_create(
            nickname=player,
            defaults={
                "email": info["email"],
                "bio": info["bio"],
                "race": race,
                "guild": guild})


if __name__ == "__main__":
    main()
