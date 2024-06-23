import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as f:
        players = json.load(f)

    for nickname, fields in players.items():
        race_info = fields["race"]
        guild_info = fields["guild"]

        race, _ = Race.objects.get_or_create(
            name=race_info["name"],
            description=race_info["description"])

        for skill in race_info["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race,
            )
        if guild_info:
            guild, _ = Guild.objects.get_or_create(
                name=guild_info["name"],
                description=guild_info["description"])
        else:
            guild = None

        Player.objects.create(
            nickname=nickname,
            email=fields["email"],
            bio=fields["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
