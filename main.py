import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild
import json


def main() -> None:
    with open("players.json", "r") as f:
        players = json.load(f)

    for player, data in players.items():

        race_data = data["race"]
        race_query = Race.objects.filter(name=race_data["name"])
        if not race_query.exists():
            race = Race.objects.create(
                name=race_data["name"],
                description=race_data["description"]
            )
        else:
            race = race_query.first()

        skills_data = race_data["skills"]
        for skill in skills_data:
            skill_query = Skill.objects.filter(name=skill["name"], race=race)
            if not skill_query.exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )

        guild = data["guild"]
        if guild:
            guild_query = Guild.objects.filter(name=guild["name"])
            if not guild_query.exists():
                guild = Guild.objects.create(
                    name=guild["name"],
                    description=guild["description"]
                )
            else:
                guild = guild_query.first()

        player_query = Player.objects.filter(nickname=player)
        if not player_query.exists():
            Player.objects.create(
                nickname=player,
                email=data["email"],
                bio=data["bio"],
                race=race,
                guild=guild,
            )


if __name__ == "__main__":
    main()
