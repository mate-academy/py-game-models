import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as f:
        players = json.load(f)
        for player_nick, player in players.items():
            race_data = player.get("race")
            guild_data = player.get("guild")
            race, _ = Race.objects.get_or_create(
                name=race_data["name"],
                defaults={
                    "description": race_data.get("description", "")
                }
            )
            guild = None
            if guild_data:
                guild, _ = Guild.objects.get_or_create(
                    name=guild_data["name"],
                    defaults={
                        "description": guild_data.get("description", "")
                    }
                )
            for each_skill in race_data["skills"]:
                Skill.objects.get_or_create(name=each_skill["name"],
                                            defaults={
                                                "bonus": each_skill["bonus"],
                                                "race": race})
            Player.objects.get_or_create(nickname=player_nick,
                                         defaults={"email": player["email"],
                                                   "bio": player["bio"],
                                                   "race": race,
                                                   "guild": guild})


if __name__ == "__main__":
    main()
