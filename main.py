import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players = json.load(file)

    for player_nick, player_data in players.items():
        email, bio, race_data, guild_data = player_data.values()
        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            description=race_data["description"]
        )
        for skill_data in race_data["skills"]:
            skill, _ = Skill.objects.get_or_create(
                name=skill_data["name"],
                bonus=skill_data["bonus"],
                race=race
            )
        guild = None
        if guild_data:
            guild, _ = Guild.objects.get_or_create(**guild_data)

        Player.objects.create(
            nickname=player_nick,
            email=email,
            bio=bio,
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
