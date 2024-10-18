import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r", encoding="utf-8") as players_file:
        players = json.load(players_file)

    for player, info in players.items():
        nickname = player
        email = info["email"]
        bio = info["bio"]
        race = info["race"]
        skills = race["skills"]
        guild = info["guild"]

        if race:
            player_race, race_created = Race.objects.get_or_create(
                name=race["name"],
                description=race["description"],
            )

        if guild:
            player_guild, guild_created = Guild.objects.get_or_create(
                name=guild["name"],
                description=guild["description"],
            )
        else:
            player_guild = None

        if skills:
            for skill in skills:
                player_skill, skill_created = Skill.objects.get_or_create(
                    name=skill["name"],
                    defaults={"bonus": skill["bonus"], "race": player_race},
                )

        player_instance, player_created = Player.objects.get_or_create(
            email=email,
            defaults={
                "nickname": nickname,
                "bio": bio,
                "race": player_race,
                "guild": player_guild,
            }
        )

    print(Player.objects.values_list(
        "nickname", "email", "bio", "race__name", "guild__name"
    ))


if __name__ == "__main__":
    main()
