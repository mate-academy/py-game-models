import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        players = json.load(f)

    for player, value in players.items():
        nickname = player
        email = value.get("email")
        bio = value.get("bio")
        race = value.get("race")
        race_name = race.get("name")
        race_description = race.get("description", None)
        skills = race.get("skills")
        guild = value.get("guild")

        race_obj, _ = Race.objects.get_or_create(
            name=race_name,
            defaults={"description": race_description}
        )
        race_id = race_obj.id

        if skills:
            for skill in skills:
                Skill.objects.get_or_create(
                    name=skill.get("name"),
                    defaults={"bonus": skill.get("bonus"),
                              "race_id": race_id},
                )

        if guild is not None:
            guild_name = guild.get("name")
            guild_description = guild.get("description", None)

            guild_obj, _ = Guild.objects.get_or_create(
                name=guild_name, defaults={"description": guild_description}
            )
            guild_id = guild_obj.id
        else:
            guild_id = None

        Player.objects.get_or_create(
            nickname=nickname, defaults={
                "email": email, "bio": bio,
                "race_id": race_id,
                "guild_id": guild_id
            }
        )


if __name__ == "__main__":
    main()
