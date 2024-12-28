from json import load

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as players_json:
        players_data = load(players_json)

    for nickname in players_data:
        race, _ = Race.objects.get_or_create(
            name=players_data[nickname]["race"]["name"],
            description=players_data[nickname]["race"]["description"]
        )

        for skill_data in players_data[nickname]["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill_data["name"],
                bonus=skill_data["bonus"],
                race=race
            )

        guild_data = players_data[nickname].get("guild")

        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=players_data[nickname]["guild"]["name"],
                description=players_data[nickname]["guild"]["description"],
            )
        else:
            guild = None

        Player.objects.get_or_create(
            nickname=nickname,
            email=players_data[nickname]["email"],
            bio=players_data[nickname]["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
