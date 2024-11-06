import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        players_data = json.load(f)

    for key in players_data:
        race, created = Race.objects.get_or_create(
            name=players_data[key]["race"]["name"],
            defaults={"description":
                          players_data[key]["race"].get("description", "")}
        )
        for elem in players_data[key]["race"]["skills"]:
            skills, created = Skill.objects.get_or_create(
                name=elem["name"],
                defaults={"bonus": elem["bonus"], 'race': race}
            )
        guild_data = players_data[key].get("guild")
        if guild_data:
            guild, created = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data.get("description")}
            )
        else:
            guild = None
        player = Player.objects.get_or_create(
            nickname=key,
            defaults={
                "email": players_data[key]["email"],
                "bio": players_data[key]["bio"],
                "race": race,
                "guild": guild

            }
        )
if __name__ == "__main__":
    main()
