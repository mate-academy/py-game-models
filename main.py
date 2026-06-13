import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players_data = json.load(file)

    for nickname, player_data in players_data.items():
        race, is_created_race = Race.objects.get_or_create(
            name=player_data["race"]["name"],
            description=player_data["race"]["description"],
        )
        if is_created_race:
            for skill_data in player_data["race"]["skills"]:
                Skill.objects.get_or_create(
                    name=skill_data["name"],
                    bonus=skill_data["bonus"],
                    race=race,
                )

        player = Player.objects.create(
            nickname=nickname,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race
        )

        guild_data = player_data.get("guild")
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                description=guild_data["description"],
            )
            player.guild = guild
            player.save()


if __name__ == "__main__":
    main()
