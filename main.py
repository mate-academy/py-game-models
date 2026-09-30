import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:

    with open("players.json", "r") as work_file:
        players = json.load(work_file)

    for player in players:
        nickname = player
        player_data = players[player]

        email = player_data["email"]
        bio = player_data["bio"]
        race = player_data["race"]

        race_name = race["name"]
        race_description = race["description"]

        race_player, _ = Race.objects.get_or_create(
            name=race_name,
            description=race_description
        )

        skills = race["skills"]

        for skill in skills:
            skills_name = skill["name"]
            skills_bonus = skill["bonus"]
            Skill.objects.get_or_create(
                name=skills_name,
                bonus=skills_bonus,
                race=race_player
            )

        guild = player_data.get("guild")
        if guild:
            guild_name = guild["name"]
            guild_description = guild["description"]

            guild_player, _ = Guild.objects.get_or_create(
                name=guild_name,
                description=guild_description
            )
        else:
            guild_player = None

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": email,
                "bio": bio,
                "race": race_player,
                "guild": guild_player
            }
        )


if __name__ == "__main__":
    main()
