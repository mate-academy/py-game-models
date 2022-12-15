import json
import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as players:
        players_data = json.load(players)
    for person in players_data:
        email_to_add = players_data[person]["email"]
        bio_to_add = players_data[person]["bio"]
        race_to_add = players_data[person]["race"]
        guild_to_add = players_data[person]["guild"]
        skill_to_add = players_data[person]["race"]["skills"]
        if not Race.objects.filter(
            name=race_to_add["name"], description=race_to_add["description"]
        ).exists():
            player_race = Race.objects.create(
                name=race_to_add["name"],
                description=race_to_add["description"]
            )
        if players_data[person]["guild"]:
            if not Guild.objects.filter(name=guild_to_add["name"]).exists():
                player_guild = Guild.objects.create(
                    name=guild_to_add["name"],
                    description=guild_to_add["description"]
                )
        for skill in skill_to_add:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"], bonus=skill["bonus"], race=player_race
                )
        Player.objects.create(
            nickname=person,
            email=email_to_add,
            bio=bio_to_add,
            race=player_race,
            guild=player_guild if players_data[person]["guild"] else None,
        )


if __name__ == "__main__":
    main()
