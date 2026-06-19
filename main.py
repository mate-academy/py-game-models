import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        players_data = json.load(f)

    for nickname, player_data in players_data.items():
        email = player_data["email"]
        bio = player_data["bio"]
        race_data = player_data["race"]

        race_name = race_data["name"]
        race_description = race_data["description"]
        skills_data = race_data["skills"]

        race, _ = Race.objects.get_or_create(
            name=race_name,
            defaults={"description": race_description},
        )

        for skill_data in skills_data:
            name = skill_data["name"]
            bonus = skill_data["bonus"]

            skill, _ = Skill.objects.get_or_create(
                name=name,
                defaults={"bonus": bonus,
                          "race": race,
                          },
            )

        guild_data = player_data.get("guild")
        if guild_data:
            guild_name = guild_data["name"]
            guild_description = guild_data["description"]

            guild, _ = Guild.objects.get_or_create(
                name=guild_name,
                defaults={
                    "description": guild_description},
            )
        else:
            guild = None

        player, _ = Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": email,
                "bio": bio,
                "race": race,
                "guild": guild,
            },
        )


if __name__ == "__main__":
    main()
