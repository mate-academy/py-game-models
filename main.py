import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as f:
        data = json.load(f)
    for player, p_data in data.items():
        races, created = Race.objects.get_or_create(
            name=p_data["race"]["name"],
            description=p_data["race"]["description"],
        )

        guild_data = p_data.get("guild") or None

        if guild_data:
            guilds, created = Guild.objects.get_or_create(
                name=guild_data["name"],
                description=guild_data.get("description"),
            )
        else:
            guilds = guild_data

        Player.objects.create(
            nickname=player,
            email=p_data["email"],
            bio=p_data["bio"],
            race=races,
            guild=guilds
        )

        for skill in p_data["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=races
            )


if __name__ == "__main__":
    main()
