import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for name in data:
        player_race, created = Race.objects.get_or_create(
            name=data[name]["race"]["name"],
            description=(
                data[name]["race"]["description"]
                if data[name]["race"].get("description")
                else ""
            )
        )
        if data[name]["guild"]:
            player_guild, created = Guild.objects.get_or_create(
                name=data[name]["guild"]["name"],
                description=(
                    data[name]["guild"]["description"]
                    if data[name]["guild"].get("description")
                    else None
                )
            )
        else:
            player_guild = None

        if data[name]["race"].get("skills"):
            for skill in data[name]["race"]["skills"]:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=player_race,
                )

        Player.objects.create(
            nickname=name,
            email=data[name]["email"],
            bio=data[name]["bio"],
            race=player_race,
            guild=player_guild
        )


if __name__ == "__main__":
    main()
