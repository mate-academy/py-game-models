import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r", encoding="utf-8") as file:
        players_data = json.load(file)

    for nickname, player_data in players_data.items():
        race_data = player_data["race"]
        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data["description"]})

        guild = None
        if player_data["guild"]:
            guild_data = player_data["guild"]
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data["description"]})
        for skill_data in race_data["skills"]:
            Skill.objects.get_or_create(name=skill_data["name"],
                                        defaults={"bonus": skill_data["bonus"],
                                                  "race": race}
                                        )
        player, created = Player.objects.get_or_create(
            nickname=nickname,
            defaults={"email": player_data["email"],
                      "bio": player_data["bio"],
                      "race": race,
                      "guild": guild}
        )
        if created:
            print(f"Created player: {player.nickname}")
        else:
            print(f"Player already exists: {player.nickname}")


if __name__ == "__main__":
    main()
