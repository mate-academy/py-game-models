import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for player in data.values():

        race_data = player.get("race", {})
        race_obj, _ = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data.get("description", "")}
        )

        guild_data = player.get("guild")
        if guild_data:
            guild_obj, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data.get("description")}
            )
        else:
            guild_obj = None

        for skill in race_data.get("skills", []):
            skill_obj, _ = Skill.objects.get_or_create(
                name=skill["name"],
                defaults={"bonus": skill["bonus"], "race": race_obj}
            )

        player_data = player
        player_obj, created = Player.objects.get_or_create(
            nickname=player.get("nickname"),
            defaults={
                "email": player_data.get("email", ""),
                "bio": player_data.get("bio", ""),
                "race": race_obj,
                "guild": guild_obj if guild_obj else None
            }

        )


if __name__ == "__main__":
    main()
